from django.contrib import admin
from django.urls import path
from .views import *

from rest_framework.routers import SimpleRouter

routers=SimpleRouter()
routers.register('categories',CategoryViewset,basename='category')
routers.register('products',ProductViewset,basename='product')


urlpatterns = [
]+routers.urls
    # path('categories',category_list),
    # path('categories/<pk>',category_details),
    
    #path('categories',Category_list.as_view())
    #path('categories',Category_details.as_view())
    
    
##talako sata ma mathi imort simpleRouter grera ni hunxa 
#     path('categories',CategoryViewset.as_view({
#         'get':'list',
#         'post':'create'
#         })),
#     path('categories/<pk>',CategoryViewset.as_view({
#         'get':'retrieve',
#         'put':'update',
#         'delete':'destroy'
#         })),
# 
