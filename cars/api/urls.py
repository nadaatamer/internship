from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, CarListCreateView, CarUpdateView, AllCarsListView, CarDeleteView

router = DefaultRouter()
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/cars/', CarListCreateView.as_view(), name='car-list-create'),
    path('api/cars/<int:pk>/', CarUpdateView.as_view(), name='car-update'),
    path('api/cars/all/', AllCarsListView.as_view(), name='all-cars-list'),
    path('api/cars/delete/<int:pk>/', CarDeleteView.as_view(), name='car-delete'),
]