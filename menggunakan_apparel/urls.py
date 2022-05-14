from django.urls import path 
from .views import list_pemain_menggunakan_apparel, list_admin_menggunakan_apparel

urlpatterns = [
    path('admin/list_menggunakan_apparel', list_admin_menggunakan_apparel, name='list_admin_menggunakan_apparel'),
    path('pemain/list_menggunakan_apparel', list_pemain_menggunakan_apparel, name='list_pemain_menggunakan_apparel'),
]