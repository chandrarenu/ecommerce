from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

# Create your views here.

# class CategoryDetails(APIView):
#     def get(self,request,pk):
#         category=get_object_or_404(Category,pk=pk)
#         serializer=CategorySerializer(category)
#         return Response(
#             serializer.data,
#         )
        

# @api_view(['GET','POST'])
# def category_list(request):
    
#     if request.method=='GET':
#         categories=Category.objects.all()
#         serializer=CategorySerializer(categories,many=True)
#         return Response(serializer.data)
    
#     else:
#         serializer=CategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             'details':
#                 "New Category created",
#         },
        
#         status=status.HTTP_201_CREATED)
            
#         # return Response({
#         #     'error':'Error in creating new category',
#         # })


# @api_view(['GET','DELETE','PUT'])
# def category_details(request,pk):
#     category=get_object_or_404(Category,pk=pk)
#     if request.method=="GET":
#         serializer=CategorySerializer(category)
#         return Response(
#             serializer.data,
#         )
#     if request.method=="DELETE":
#         category.delete()
#         return Response(
#             status=status.HTTP_204_NO_CONTENT
            
#         )
        
#     if request.method=="PUT":
#         serializer=CategorySerializer(category,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(
#             {
#                 'details':'data has been updated'
#             }
#         )
        
class CategoryList(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer