from django.shortcuts import render
from django.http import HttpResponse

from .models import Destination


def index(request):

    des1= Destination()
    des1.desc= 'The city that never sleep'
    des1.city='Marrakech'
    des1.price=800


    return render (request, 'index.html',{'des1':des1})

# Create your views here.
