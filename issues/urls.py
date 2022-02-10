from django.contrib import admin
from django.urls import path,include
from . import views
from .router import router


urlpatterns = [
    path('api/',include(router.urls)),
    path('api/auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('',views.home),
    ## testing
    path('customer',views.customer),
    path('products',views.products),
]
