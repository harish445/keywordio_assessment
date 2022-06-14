from rest_framework import serializers
from library.models import Book
from djoser.serializers import UserCreateSerializer, UserSerializer
from . models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('email', 'username', 'password')