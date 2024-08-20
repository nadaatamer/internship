# file is a Django REST Framework (DRF) serializer that converts complex data types, such as Django models, into native Python data types that can then be easily rendered into JSON, XML, or other content types. 
# It also provides deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.

from rest_framework import serializers
from cars.models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta: #This inner class is used to specify metadata options for the CarSerializer.
        model = Car #specifying the model to be serialized
        fields = '__all__' 