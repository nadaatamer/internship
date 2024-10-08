from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from cars.models import Car
from .serializers import CarSerializer
#import logging

#post: crfeate new car obj from provided data & handling validation errors
#get: retrievesz and returns the list of car objs
@api_view(['GET', 'POST']) #decorator specifies that the view function can handle GET and POST requests
#decorator alllows modifying behavior function, to add functionality
def car_list_create_view(request): #defining http arg
    if request.method == 'GET':
        cars = Car.objects.all()
        #serializes the list of car objects into json format
        serializer = CarSerializer(cars, many=True)
        return Response({'message': 'List of cars retrieved successfully', 'cars': serializer.data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        #deserializes json format into car
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() #save new car into database
            return Response({'message': 'Car created successfully', 'car': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#record log messages generated by an application. 
#logger = logging.getLogger(__name__)

@api_view(['GET', 'DELETE', 'PUT'])
def car_detail_view(request, pk):
    try:
        #handle the case where a car pk doesnt exist in db
        car = Car.objects.get(pk=pk) #retrieve data using pk
    except Car.DoesNotExist:
        return Response({'message': 'Car not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarSerializer(car)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Car updated successfully', 'car': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        car.delete()
        return Response({'message': 'Car deleted successfully'}, status=status.HTTP_204_NO_CONTENT)