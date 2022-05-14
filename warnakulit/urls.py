from django.urls import path 
from .views import pemain_read_warna_kulit, admin_read_warna_kulit

urlpatterns = [
    path('admin/list_warna_kulit', admin_read_warna_kulit, name='admin_read_warna_kulit'),
    path('pemain/list_warna_kulit', pemain_read_warna_kulit, name='pemain_read_warna_kulit'),
]
