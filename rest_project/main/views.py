from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import  Product
from rest_framework import viewsets
from main.serializers import UserSerializer, GroupSerializer, ProductSerializer

class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited"""
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """API endpoint that allows groups to be viewed or edited"""
    queryset = Group.objects.all().order_by('-id')
    serializer_class = GroupSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """API endpoint that allows groups to be viewed or edited"""
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
