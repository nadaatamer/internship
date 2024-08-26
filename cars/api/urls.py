from django.urls import path
from .views import car_list_create_view, car_detail_view

urlpatterns = [
    path('cars/', car_list_create_view, name='car-list-create'),
    path('cars/<int:pk>/', car_detail_view, name='car-detail'),
]