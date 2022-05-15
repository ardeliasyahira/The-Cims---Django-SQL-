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
from .views import pemain_read_koleksi, admin_read_koleksi, create_koleksi, delete_koleksi, update_koleksi

urlpatterns = [
    path('admin/list_koleksi', admin_read_koleksi, name='admin_read_koleksi'),
    path('pemain/list_koleksi', pemain_read_koleksi, name='pemain_read_koleksi'),
    path('admin/create_koleksi', create_koleksi, name='create_koleksi'),
    path('admin/delete_koleksi', delete_koleksi, name='delete_koleksi'),
    path('admin/update_koleksi', update_koleksi, name='update_koleksi'),
]

