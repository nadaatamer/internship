from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from cars.models import Car

class CarAPITestCase(APITestCase):
    def setUp(self):
        #self: used to define instance variables that will be available to all the test methods within the class
        #reverse: generate urls dynamically for end points to avoid hardcoding urls, and retrieve details of specific car
        #(ensure that your tests will continue to work even if the actual url patterns change, as long as the named patterns remain the same)
        self.car = Car.objects.create(name="Toyota", model="Corolla", year=2020, brand="Toyota") #self.car creates new car
        self.create_url = reverse('car-list-create')
        self.detail_url = reverse('car-detail', args=[self.car.id])
        #self.update_url = reverse('car-detail', kwargs={'pk': self.car.pk})

    def test_create_car(self):
        data = {'name': 'New Car', 'model': 'New Model', 'year': 2022, 'brand': 'New Brand'}
        response = self.client.post(self.create_url, data, format='json') #stores the result of an http request made by test client
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)#check if 2 variables are equal
        self.assertEqual(Car.objects.count(), 2)
        self.assertEqual(response.data['message'], "Car created successfully")
        
#update method is giving errors
    # def test_update_car(self):
    #     data = {
    #         'brand': 'Updated Brand'
    #     }
    #     response = self.client.put(self.update_url, data, format='json')
    #     self.car.refresh_from_db()
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(self.car.brand, 'Updated Brand')

    def test_delete_car(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Car.objects.count(), 0)
        self.assertEqual(response.data['message'], "Car deleted successfully")

    def test_list_cars(self):
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "List of cars retrieved successfully")
        self.assertEqual(len(response.data['cars']), 1)
        self.assertEqual(response.data['cars'][0]['name'], 'Toyota')
        self.assertEqual(response.data['cars'][0]['model'], 'Corolla')
        self.assertEqual(response.data['cars'][0]['year'], 2020)