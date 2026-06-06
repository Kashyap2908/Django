from django.shortcuts import render
from .models import Product
# Create your views here.
def home(request):
    products={}
    if request.GET.get('search'):
        products=Product.objects.filter(name__icontains=request.GET.get('search'))
    else:
        products=Product.objects.all()

    return render(request,'home.html',{'products':products})