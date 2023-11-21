from rest_framework import serializers;
from .models import User, Service;

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        # app_label = "ordain_app"
        model = User
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
    