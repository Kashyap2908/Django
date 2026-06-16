from django.shortcuts import render
from events.models import Events

# Create your views here.
def category(req):
    c = Events.objects.values_list('Category', flat=True).distinct()
    return render(req,'category.html',{'c':c})