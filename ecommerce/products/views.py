from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from .models import Product,Category
from rest_framework.response import Response
from .serializers import ProductSerializer,CategorySerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['GET', 'POST'])
def apiOverview(request):
    api_urls = {
        'List':'/product-list/',
        'Detail View':'product-detail/<str:pk>/',
        'Create':'product-create/',
        'Update':'product-update/<str:pk>/',
        'Delete':'product-detlete/<str:pk>/',
    }
    return Response(api_urls)



@api_view(['GET'])
def productList(request):
    tasks = Product.objects.all()
    serializer = ProductSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def productDetail(request,pk):
    tasks = Product.objects.get(id=pk)
    serializer = ProductSerializer(tasks,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def productCreate(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def productUpdate(request,pk):
    task = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated]) 
def productDelete(request,pk):
    task = Product.objects.get(id=pk)
    task.delete()
    return Response("item sucessfully")



#category list api
@api_view(['GET'])
def categoryList(request):
    tasks = Category.objects.all()
    serializer = CategorySerializer(tasks,many=True)
    return Response(serializer.data)

