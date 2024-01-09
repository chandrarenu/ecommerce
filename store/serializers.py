from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']  

# class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
    
#     def create(self, validated_data):
#         isinstance=Category.objects.create(**validated_data)
#         return isinstance
    
#     def update(self, instance, validated_data):
#         instance.name=validated_data.get('name')
#         instance.save()
#         return instance
        