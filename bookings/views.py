from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Restaurant, Table, Booking, MenuItem
from django.urls import reverse_lazy

# Create your views here.

# Restaurant Views

class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurant_list.html'

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
