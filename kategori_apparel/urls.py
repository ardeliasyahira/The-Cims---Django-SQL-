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
from .views import pemain_read_kategoriapparel, admin_read_kategoriapparel, create_kategori_apparel, delete_kategori_apparel

urlpatterns = [
    path('admin/list_kategoriapparel', admin_read_kategoriapparel, name='admin_read_kategoriappparel'),
    path('pemain/list_kategoriapparel', pemain_read_kategoriapparel, name='pemain_read_kategoriapparel'),
    path('admin/create_kategoriapparel', create_kategori_apparel, name='create_kategori_apparel'),
    path('admin/delete_kategoriapparel', delete_kategori_apparel, name='delete_kategori_apparel'),
]

