from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status , generics, mixins
from rest_framework.views import APIView


# Create your views here.


class CategoryList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    
    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
        
# class CategoryList(APIView):
    
#     def get(self,request):
#         categories=Category.objects.all()
#         serializers=self.serializer_class(categories,many=True)
#         return Response(serializers.data)
    
    # def post(self,request):
    #     serializer=CategorySerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({
    #         'details':
    #             "New category created",
    #     },
        
    #     status=status.HTTP_201_CREATED)
    
        
class CategoryDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
   
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    
    def get(self,request,*args,**kwrags):
            return self.retrieve(request,*args,**kwrags)
        
    def put(self,request,*args,**kwargs):
        return self.update()
    
    def delete(self,request,*args,**kwargs):
        return self.destroy() 

# class CategoryDetail(APIView):
    
#     def get(self,request,pk):
#         category=get_object_or_404(category,pk=pk)
        
#         serializer=CategorySerializer(category)
#         return Response(
#             serializer.data,
#         )
#     def put(self,request,pk):
#         category=get_object_or_404(Category,pk=pk)
#         serializer=CategorySerializer(category,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(
#             {
#                 'details':'data has been updated'
#             }
#         )
        
#     def delete(self,request,pk):
#         category=get_object_or_404(Category,pk=pk)
#         category.delete()
#         return Response(
#             status=status.HTTP_204_NO_CONTENT
#         )
# class ProductViewset(viewsets.ModelViewSet):
#     queryset=Product.ibjects.all()
#     serializer_class=ProductSerializer
        

        
    

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
        
