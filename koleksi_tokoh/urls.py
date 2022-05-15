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
from .views import pemain_read_koleksi_tokoh, admin_read_koleksitokoh, create_koleksi_tokoh, delete_koleksi_tokoh

urlpatterns = [
    path('admin/list_koleksitokoh', admin_read_koleksitokoh, name='admin_read_koleksitokoh'),
    path('pemain/list_koleksitokoh', pemain_read_koleksi_tokoh, name='pemain_read_koleksi_tokoh'),
    path('admin/create_koleksitokoh', create_koleksi_tokoh, name='create_koleksi_tokoh'),
    path('admin/delete_koleksitokoh', delete_koleksi_tokoh, name='delete_koleksi_tokoh'),
]

