from django.shortcuts import render
from .models import Mangue

# Create your views here.



def home(request):
    obj = Mangue.objects.all().count()
    return render(request, 'index.html', {'obj':obj})
    