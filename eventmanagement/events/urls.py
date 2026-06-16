from django.urls import path
from . import views

urlpatterns = [
    path('',views.events,name='home'),
    path('add/',views.add,name='add')
]
