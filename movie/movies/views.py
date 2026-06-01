from os import name

from django.shortcuts import render
from httpcore import request
from .models import Movie

# Create your views here.
def home(request):
    return render(request, 'home.html')

def get(request):
    return render(request, 'get.html') 

def add(request):
    name=request.GET.get('name')
    release_date=request.GET.get('release_date')
    rating=request.GET.get('rating')
    Movie.objects.create(name=name, release_date=release_date, rating=rating)
    return render(request, 'get.html')

def show(request):
    m=Movie.objects.all()
    return render(request, 'show.html', {'m': m})

def search(request):
    name=request.GET.get('name')
    if name:
        m=Movie.objects.filter(name__icontains=name)
    else:
        m=Movie.objects.all()
    return render(request, 'search.html', {'m': m})