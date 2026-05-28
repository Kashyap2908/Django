from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello Kashyap, You are in Home page of app1")


def about(request):
    return HttpResponse("Hello Kashyap, You are in About page of app1")

def contact(request):
    return HttpResponse("Contact us on 63535815**- Kashyap")

def home1(request):
    return render(request,'1.html')