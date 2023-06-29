from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Restaurant, Table, Booking, MenuItem, Profile
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BookingForm
from django.views import View
from django.utils.decorators import method_decorator
from django.db.models import Sum
from django.db.models import Case, When, Value, CharField
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib import messages


# Gallery View.


class GalleryView(TemplateView):
    template_name = 'gallery.html'


# Restaurant Views

class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'home.html'


class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = 'restaurant_detail.html'


class RestaurantCreateView(CreateView):
    model = Restaurant
    template_name = 'restaurant_new.html'
    fields = ('name', 'address', 'opening_time', 'closing_time')


class RestaurantUpdateView(UpdateView):
    model = Restaurant
    template_name = 'restaurant_edit.html'
    fields = ('name', 'address', 'opening_time', 'closing_time')


class RestaurantDeleteView(DeleteView):
    model = Restaurant
    template_name = 'restaurant_delete.html'
    success_url = reverse_lazy('restaurant_list')


# User Views

class CustomLoginView(LoginView):
    def get_success_url(self):
        url = super().get_success_url()
        if self.request.user.is_superuser:
            url = reverse('adminapp:home')  # Use the name you defined in urls.py
        return url


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    
# class CustomLoginView(auth_views.LoginView):
#     def get_success_url(self):
#         url = super().get_success_url()
#         if self.request.user.is_superuser:
#             return '/superuser_dashboard'  # Replace with the URL of your superuser dashboard
#         return url
    

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookings'] = Booking.objects.filter(user=self.request.user)
        messages.success(self.request, 'Your booking was successful!')
        return context
 
# Booking Views

class BookingListView(ListView):
    model = Booking
    template_name = 'booking_list.html'

class BookingDetailView(DetailView):
    model = Booking
    template_name = 'booking_detail.html'


@method_decorator(login_required, name='dispatch')
class BookingCreateView(View):
    def get_slots(self):
        # Get all bookings, grouped by date and time
        bookings = (
            Booking.objects.values('date', 'time')
            .annotate(guests=Sum('guests'))
            .order_by('date', 'time')
        )

        # Create list of unavailable time slots
        unavailable_slots = []
        guests_on_date = 0
        current_date = None

        for b in bookings:
            if b['date'] != current_date:
                # Start of a new day
                guests_on_date = 0
                current_date = b['date']

            guests_on_date += b['guests']

            if guests_on_date > 24:
                unavailable_slots.append({'date': b['date'], 'time': b['time']})

        return unavailable_slots

    def get(self, request):
        form = BookingForm()

        # Call the get_slots method to get the unavailable slots
        unavailable_slots = self.get_slots()

        return render(request, 'booking_new.html', {
            'form': form,
            'unavailable_slots': unavailable_slots
        })

    def post(self, request):
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            try:
                restaurant = Restaurant.objects.get(name="DeAngelo's")
                booking.restaurant = restaurant
                booking.save()
                form.save_m2m()  # This line is new
                return redirect('profile')
            except Restaurant.DoesNotExist:
                form.add_error('restaurant', 'This restaurant does not exist.')
                
        return render(request, 'booking_new.html', {'form': form})


class BookingUpdateView(UpdateView):
    model = Booking
    template_name = 'booking_edit.html'
    fields = ('user', 'restaurant', 'table', 'date', 'time', 'guests', 'status')

# class BookingDeleteView(DeleteView):
#     model = Booking
#     template_name = 'booking_delete.html'
#     success_url = reverse_lazy('booking_list')

@login_required
def cancel_booking(request, pk):
    try:
        booking = Booking.objects.get(pk=pk)
        if booking.user == request.user:  # Ensure the logged-in user owns this booking
            booking.delete()
        else:
            return redirect('error')  # You may want to handle this case differently
    except Booking.DoesNotExist:
        pass  # You may want to handle this case differently
    return redirect('profile')  # Redirect to the profile page
    
def get_slots(request):
    # Get all bookings, grouped by date and time
    bookings = (
        Booking.objects.values('date', 'time')
        .annotate(guests=Sum('guests'))
        .order_by('date', 'time')
    )

    # Create lists of available and unavailable time slots
    available_slots = []
    unavailable_slots = []
    guests_on_date = 0
    current_date = None

    for b in bookings:
        if b['date'] != current_date:
            # Start of a new day
            guests_on_date = 0
            current_date = b['date']

        guests_on_date += b['guests']

        if guests_on_date <= 24:
            available_slots.append({'date': b['date'], 'time': b['time']})
        else:
            unavailable_slots.append({'date': b['date'], 'time': b['time']})

    return render(request, 'slots.html', {
        'available_slots': available_slots,
        'unavailable_slots': unavailable_slots
    })
    
class CheckTableAvailabilityView(View):
    def get(self, request, *args, **kwargs):
        table_id = request.GET.get('table_id')
        date = request.GET.get('date')
        time = request.GET.get('time')
        
        # Convert date and time strings to datetime objects, 
        # you might need to adjust the format depending on how you're sending the date and time
        date = datetime.strptime(date, "%Y-%m-%d").date()
        time = datetime.strptime(time, "%H:%M").time()
        
        # Check for overlapping bookings
        overlapping_bookings = Booking.objects.filter(
            restaurant=self.restaurant,
            date=date,
            tables__id=table_id,
            time=time,
        )

        if overlapping_bookings.exists():
            return JsonResponse({'is_available': False})
        else:
            return JsonResponse({'is_available': True})


# Menu views

class MenuListView(ListView):
    model = MenuItem
    template_name = 'menu.html'  
    context_object_name = 'menu_items'
    
    def get_queryset(self):
        return MenuItem.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['starters'] = MenuItem.objects.filter(category='ST')
        context['pizzas'] = MenuItem.objects.filter(category='PI')
        context['pastas'] = MenuItem.objects.filter(category='PA')

        return context

