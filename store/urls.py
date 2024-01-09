from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('categories',category_list),
    path('categories/<pk>',category_details),
]
