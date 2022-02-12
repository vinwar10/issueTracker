from django.contrib import admin
from django.urls import path,include
from . import views
from .router import router
from .api.viewsets import RegisterViewAPI 

urlpatterns = [
    path('api/',include(router.urls)),
    path('api/auth/',include('rest_framework.urls',namespace='rest_framework'),{'next_page':'api/user/'}),
    path('api/auth/register/',RegisterViewAPI.as_view(),name = 'register'),
    path('',views.home),
    ## testing
    path('customer',views.customer),
    path('products',views.products),
]
