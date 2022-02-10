from django.shortcuts import render
from mangue.views import home

# Create your views here.


def home1(request):
    return home(request)