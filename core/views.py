from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .serializers import *


User=get_user_model()

# Create your views here.

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.validated_data.get('email')
    password = serializer.validated_data.get('password')
    
    user=User.objects.create_user(email=email,password=password)
    
    if user:
        return Response('user has been created')
    return Response("something went wrong")
    
    
    
#     email = request.data.get('email')
 #     password = request.data.get('password')
   
#     if User.objects.filter(username=username).exists():
#        return Response({'Username already exists'})
   
#    # Create a new user
#     user = User.objects.create_user(username=username, password=password)
 
#    # Create a token for the user
#     token, _ = Token.objects.get_or_create(user=user)

#     return Response({
#         'user': user.get_username(),
#         'token': token.key
#     })
    


@api_view(['POST'])
def login(request):
    email=request.data.get('email')
    password=request.data.get('password')
    
    
    
    
    user=authenticate(username=email,password=password)
    
    if user:
        # Create a token for the user
        token,_=Token.objects.get_or_create(user=user)
        return Response({
            'user':user.get_username(),
            'token':token.key
        })
    return Response("invalid")
