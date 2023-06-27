from django.shortcuts import render
from django.views import View 
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from bookings.models import Table, Booking, MenuItem
from django.urls import reverse, reverse_lazy
from .mixins import AdminRequiredMixin
from bookings.models import Table, Restaurant

class AdminHomeView(AdminRequiredMixin, View):
    def get(self, request):
        return render(request, 'adminapp/home.html')

class TableAdminListView(AdminRequiredMixin, ListView):
    model = Table
    context_object_name = 'tables'
    template_name = 'adminapp/table_list.html'
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(context['tables'])  # This should print the queryset to the console
    #     return context


class TableAdminCreateView(AdminRequiredMixin, CreateView):
    model = Table
    fields = ['table_number', 'seats']  # Include any other fields you have in your Table model
    success_url = reverse_lazy('adminapp:table-list')  # Redirect to table list after a successful creation
    template_name = 'adminapp/table_form.html'
    
    def form_valid(self, form):
        # Replace 'some_restaurant' with the actual Restaurant instance
        some_restaurant = Restaurant.objects.get(pk=1)  # for example
        form.instance.restaurant = some_restaurant
        return super().form_valid(form)
    

class TableAdminUpdateView(UpdateView):
    model = Table
    template_name = 'adminapp/table_edit.html'
    fields = ['table_number', 'seats']
    success_url = '/adminapp/table/'


class TableAdminDeleteView(AdminRequiredMixin, DeleteView):
    model = Table
    template_name = 'adminapp/table_delete.html'
    success_url = '/adminapp/table/'


class BookingAdminListView(AdminRequiredMixin, ListView):
    model = Booking
    template_name = 'adminapp/booking_list.html'


class BookingAdminCreateView(AdminRequiredMixin, CreateView):
    model = Booking
    # ... other CreateView options


class BookingAdminUpdateView(AdminRequiredMixin, UpdateView):
    model = Booking
    template_name = 'adminapp/booking_update.html'
    fields = ['table', 'date', 'time', 'party_size']  # replace these with your actual Booking fields

    def get_success_url(self):
        return reverse('adminapp:booking-detail', kwargs={'pk': self.object.pk})

 
class BookingAdminDeleteView(AdminRequiredMixin, DeleteView):
    model = Booking
    template_name = 'adminapp/booking_delete.html'

    def get_success_url(self):
        return reverse('adminapp:booking-list')


class MenuItemAdminListView(AdminRequiredMixin, ListView):
    model = MenuItem
    template_name = 'adminapp/menuitem_list.html'
    
    def get_queryset(self):
        return MenuItem.objects.order_by('-category')


class MenuItemAdminCreateView(AdminRequiredMixin, CreateView):
    model = MenuItem
    template_name = 'adminapp/menuitem_form.html'
    fields = ['name', 'description', 'price', 'category', 'image']
    success_url = reverse_lazy('adminapp:menuitem-list')


class MenuItemAdminUpdateView(AdminRequiredMixin, UpdateView):
    model = MenuItem
    template_name = 'adminapp/menuitem_edit.html'
    fields = ['name', 'description', 'price']  # or whatever fields you have on the MenuItem model

    def get_success_url(self):
        return reverse('adminapp:menuitem-list')


class MenuItemAdminDeleteView(AdminRequiredMixin, DeleteView):
    model = MenuItem
    template_name = 'adminapp/menuitem_delete.html'
    success_url = reverse_lazy('adminapp:menuitem-list')

