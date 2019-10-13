from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.parsers import JSONParser
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

@csrf_exempt
def product_list(requset):
    """
    List all products or create new
    """ 
    if requset.method == 'GET': 
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif requset.method == 'POST': 
        data = JSONParser().parse(requset)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid(): 
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error, status=400)

@csrf_exempt
def product_detail(requset, pk):
    """
    Retrive update or delete product
    """
    try: 
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
    if requset.method == 'GET':
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)

    elif requset.method == 'PUT':
        data = JSONParser().parse(requset)
        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.error, status=400)
    
    elif requset.method == 'DELETE':
        product.delete()
        return HttpResponse(status=204)
