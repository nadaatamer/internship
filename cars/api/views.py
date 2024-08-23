from rest_framework import generics, status
from .views import CarListCreateView, CarUpdateView, AllCarsListView, CarDeleteView
from cars.models import Car
from .serializers import CarSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all() #Specifies the queryset that this view will operate on, which is all instances of the Car model.
    serializer_class = CarSerializer

class CarUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    partial = True

class AllCarsListView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDeleteView(generics.DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Car deleted"}, status=status.HTTP_204_NO_CONTENT)