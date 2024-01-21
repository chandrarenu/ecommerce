from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
from random import randint
from .models import *


class UserSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()
    confirm_password = serializers.CharField()
    
    # #SINGLE KO LAGI MTRA 
    # def validate_password(self,value):
    #     if len(value) < 8:
    #         raise serializers.ValidationError({
    #             "The password must be greater than 8 characters"
    #         })
    #     return value
    
    def validate_email(self, value):
        user = User.objects.filter(email=value).exists()
        if user:
            raise serializers.ValidationError("This email is already in use")
        return value
        
    
    #OR YO tala VAKO GRNA MILXA N YO MULTIPLE KO LAGI JSTAI MA CONFIRM PASSWORD KO LAGI NI 
    def validate(self, attrs):
        
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError({
                'details': "The password and confirm password does not match"
            })
            
        return super().validate(attrs)