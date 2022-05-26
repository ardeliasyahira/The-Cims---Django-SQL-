from django.urls import path

from . import views

app_name = 'makanan'

urlpatterns = [
    path('', views.login, name='login'),
    path('admin_read_makanan/', views.admin_read_makanan, name='admin_read_makanan'),
    path('pemain_read_makanan/', views.pemain_read_makanan, name='pemain_read_makanan'),
]