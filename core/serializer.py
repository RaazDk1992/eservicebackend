from rest_framework import serializers
from django.contrib.auth.models import User
from .models import AppUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'
    def create(self, validated_data):
        user = AppUser.objects.create_user(validated_data['username'],validated_data['password'])
        return user



