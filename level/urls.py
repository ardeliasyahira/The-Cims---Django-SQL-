"""level URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path 
from .views import pemain_read_level, admin_read_level, create_level

urlpatterns = [
    path('admin/list_level', admin_read_level, name='admin_read_level'),
    path('pemain/list_level', pemain_read_level, name='pemain_read_level'),
    path('admin/create_level', create_level, name='create_level'),
]
