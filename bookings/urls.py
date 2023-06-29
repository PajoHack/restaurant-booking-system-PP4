from django.urls import path
from . import views
from .views import (RestaurantListView, 
                    RestaurantDetailView, RestaurantCreateView, 
                    RestaurantUpdateView, RestaurantDeleteView, 
                    MenuListView, ProfileDetailView, CheckTableAvailabilityView)


urlpatterns = [
    path('', RestaurantListView.as_view(), name='home'),
    path('restaurant/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('restaurant/new/', RestaurantCreateView.as_view(), name='restaurant_new'),
    path('restaurant/<int:pk>/edit/', RestaurantUpdateView.as_view(), name='restaurant_edit'),
    path('restaurant/<int:pk>/delete/', RestaurantDeleteView.as_view(), name='restaurant_delete'),
    path('menu/', MenuListView.as_view(), name='menu'),
    path('accounts/profile/', ProfileDetailView.as_view(), name='profile'),
    path('new/', views.BookingCreateView.as_view(), name='booking_new'),
    path('booking/cancel/<int:pk>/', views.cancel_booking, name='cancel_booking'),
    
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    
    path('check_table_availability/', CheckTableAvailabilityView.as_view(), name='check_table_availability'),
]