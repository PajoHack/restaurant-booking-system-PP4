from django.urls import path
from .views import RestaurantListView, RestaurantDetailView, RestaurantCreateView, RestaurantUpdateView, RestaurantDeleteView


urlpatterns = [
    path('', RestaurantListView.as_view(), name='home'),
    path('restaurant/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('restaurant/new/', RestaurantCreateView.as_view(), name='restaurant_new'),
    path('restaurant/<int:pk>/edit/', RestaurantUpdateView.as_view(), name='restaurant_edit'),
    path('restaurant/<int:pk>/delete/', RestaurantDeleteView.as_view(), name='restaurant_delete'),
]