from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('categories',CategoryList.as_view),
    # path('categories/<pk>',CategoryDetails.as_view),
]
