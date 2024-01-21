from rest_framework import serializers
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
    
    
    #OR YO tala VAKO GRNA MILXA N YO MULTIPLE KO LAGI JSTAI MA CONFIRM PASSWORD KO LAGI NI 
    
    def validate(self, attrs):
        
        if len(attrs.get('password')) != attrs.get('confirm_password'):
            raise serializers.ValidationError({
                'details': "The password and confirm password does not match"
            })
            
        return super().validate(attrs)