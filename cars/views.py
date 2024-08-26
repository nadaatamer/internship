# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from .models import Car
# from .serializers import CarSerializer

# class CarViewSet(viewsets.ModelViewSet):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer

#     def create(self, request, *args, **kwargs):
#         response = super().create(request, *args, **kwargs)
#         response.data['message'] = "Car created successfully"
#         return response

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response({"message": "Car deleted successfully"}, status=status.HTTP_200_OK)

#     def list(self, request, *args, **kwargs):
#         response = super().list(request, *args, **kwargs)
#         response.data = {
#             'message': "List of cars retrieved successfully",
#             'cars': response.data
#         }
#         return response
