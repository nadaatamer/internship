from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from cars.models import Car

class CarAPITestCase(APITestCase):
    def setUp(self):
        self.car = Car.objects.create(make="Toyota", model="Corolla", year=2021)
        self.list_url = reverse('car-list')
        self.detail_url = reverse('car-detail', kwargs={'pk': self.car.pk})

    def test_get_car_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_car(self):
        # removing post
        car = Car.objects.create(make="Honda", model="Civic", year=2022)
        self.assertEqual(Car.objects.count(), 2)
        self.assertEqual(car.make, "Honda")
        self.assertEqual(car.model, "Civic")
        self.assertEqual(car.year, 2022)

    def test_get_car_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_car(self):
        data = {"make": "Toyota", "model": "Corolla", "year": 2022}
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.car.refresh_from_db()
        self.assertEqual(self.car.year, 2022)

    def test_delete_car(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Car.objects.count(), 0)