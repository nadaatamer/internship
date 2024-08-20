from rest_framework import viewsets, status
from rest_framework.response import Response
from cars.models import Car
from .serializers import CarSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object() #retrieves car instance i need to delete based on url parameters
        self.perform_destroy(instance)
        return Response({"message": "Car deleted "},status=status.HTTP_204_NO_CONTENT) #deletion succeeded 

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True) #many=True shows that multiple objects are being serialized
        return Response({
            "message": "List of all cars",
            "data": serializer.data
        })

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False) #Checks if the update is partial (PATCH) or full (PUT).
        #full update(put): to replace entire resource with the new data provided, u need to provide all fields of the resource
        #partial update(patch): to update only the fields provided in the request, u need to provide only the fields u want to update
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial) #binding incoming data to retrieved car instance
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Car updated",
            "data": serializer.data
        })
    
    @action(detail=True, methods=['patch'])
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)