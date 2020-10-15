from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):

    return render(request, 'home.html',{'first_name': 'John', 'last_name': 'Doe'})

def add(request):
    num1=int(request.GET['val1'])
    num2 =int(request.GET['val2'])

    result=num1+num2
    return render (request,'result.html',{'result':result})