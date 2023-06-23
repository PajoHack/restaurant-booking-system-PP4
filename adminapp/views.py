from django.shortcuts import render
from django.views import View 
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from bookings.models import Table, Booking, MenuItem
from django.urls import reverse, reverse_lazy
from .mixins import AdminRequiredMixin


class AdminHomeView(AdminRequiredMixin, View):
    def get(self, request):
        return render(request, 'adminapp/home.html')

class TableAdminListView(AdminRequiredMixin, ListView):
    model = Table
    # ... other ListView options

class TableAdminCreateView(AdminRequiredMixin, CreateView):
    model = Table
    # ... other CreateView options

class TableAdminUpdateView(AdminRequiredMixin, UpdateView):
    model = Table
    template_name = 'adminapp/table_update.html'
    fields = ['name', 'capacity']  # or whatever fields you have on the Table model

    def get_success_url(self):
        return reverse('adminapp:table-detail', kwargs={'pk': self.object.pk})

class TableAdminDeleteView(AdminRequiredMixin, DeleteView):
    model = Table
    template_name = 'adminapp/table_delete.html'
    success_url = '/adminapp/table/'  # or wherever you want to redirect after delete

class BookingAdminListView(AdminRequiredMixin, ListView):
    model = Booking
    # ... other ListView options

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
    # ... other ListView options

class MenuItemAdminCreateView(AdminRequiredMixin, CreateView):
    model = MenuItem
    # ... other CreateView options

class MenuItemAdminUpdateView(AdminRequiredMixin, UpdateView):
    model = MenuItem
    template_name = 'adminapp/menu_item_update.html'
    fields = ['name', 'description', 'price']  # or whatever fields you have on the MenuItem model

    def get_success_url(self):
        return reverse('adminapp:menu-item-detail', kwargs={'pk': self.object.pk})

from django.urls import reverse_lazy

class MenuItemAdminDeleteView(AdminRequiredMixin, DeleteView):
    model = MenuItem
    template_name = 'adminapp/menu_item_delete.html'
    success_url = reverse_lazy('adminapp:menu-item-list')

