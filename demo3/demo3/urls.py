"""
URL configuration for demo3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import IPL.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IPL.views.blank, name='blank'),
    path('home/', IPL.views.home, name='home'),
    path('MI/', IPL.views.MI, name='MI'),
    path('GT/', IPL.views.GT, name='GT'),
    path('CSK/', IPL.views.CSK, name='CSK'),
    path('get/',IPL.views.get,name='get'),
    path('show/',IPL.views.show,name='show'),
    path('db/', IPL.views.db, name='db')
]
