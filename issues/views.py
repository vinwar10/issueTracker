from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'issues/dashboard.html')

# testing html views
def products(request):
    return render(request,'issues/products.html')

def customer(request):
    return render(request,'issues/customer.html')
