from django.urls import path
from .views import (
    TableAdminListView, TableAdminCreateView, TableAdminUpdateView, TableAdminDeleteView,
    BookingAdminListView, BookingAdminCreateView, BookingAdminUpdateView, BookingAdminDeleteView,
    MenuItemAdminListView, MenuItemAdminCreateView, MenuItemAdminUpdateView, 
    MenuItemAdminDeleteView, AdminHomeView
)

app_name = 'adminapp'

urlpatterns = [
    path('', AdminHomeView.as_view(), name='home'),
    
    path('table/', TableAdminListView.as_view(), name='table-list'),
    path('table/add/', TableAdminCreateView.as_view(), name='table-add'),
    path('table/<int:pk>/edit/', TableAdminUpdateView.as_view(), name='table-edit'),
    path('table/<int:pk>/delete/', TableAdminDeleteView.as_view(), name='table-delete'),

    path('booking/', BookingAdminListView.as_view(), name='booking-list'),
    path('booking/add/', BookingAdminCreateView.as_view(), name='booking-add'),
    path('booking/<int:pk>/edit/', BookingAdminUpdateView.as_view(), name='booking-edit'),
    path('booking/<int:pk>/delete/', BookingAdminDeleteView.as_view(), name='booking-delete'),

    path('menuitem/', MenuItemAdminListView.as_view(), name='menuitem-list'),
    path('menuitem/add/', MenuItemAdminCreateView.as_view(), name='menuitem-add'),
    path('menuitem/<int:pk>/edit/', MenuItemAdminUpdateView.as_view(), name='menuitem-edit'),
    path('menuitem/<int:pk>/delete/', MenuItemAdminDeleteView.as_view(), name='menuitem-delete'),
]

