from django.urls import path

from . import views

app_name = 'misiutama'

urlpatterns = [
    path('', views.login, name='login'),
    path('admin_read_misiutama/', views.admin_read_misiutama, name='admin_read_misiutama'),
    path('pemain_read_misiutama/', views.pemain_read_misiutama, name='pemain_read_misiutama')
]