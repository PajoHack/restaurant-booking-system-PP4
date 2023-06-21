from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Restaurant, Table, Booking, MenuItem
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Booking
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile

# Create your views here.

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

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return self.request.user.profile
 


# Booking Views

class BookingListView(ListView):
    model = Booking
    template_name = 'booking_list.html'

class BookingDetailView(DetailView):
    model = Booking
    template_name = 'booking_detail.html'

class BookingCreateView(CreateView):
    model = Booking
    template_name = 'booking_new.html'
    fields = ('user', 'restaurant', 'table', 'date', 'time', 'guests', 'status')

class BookingUpdateView(UpdateView):
    model = Booking
    template_name = 'booking_edit.html'
    fields = ('user', 'restaurant', 'table', 'date', 'time', 'guests', 'status')

class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'booking_delete.html'
    success_url = reverse_lazy('booking_list')
    

# Menu views

class MenuListView(ListView):
    model = MenuItem
    template_name = 'menu.html'  
    context_object_name = 'menu_items'
