from django.urls import path

from . import views

app_name = 'makan'

urlpatterns = [
    path('', views.login, name='login'),
    path('admin_read_makan/', views.admin_read_makan, name='admin_read_makan'),
    path('pemain_read_makan/', views.pemain_read_makan, name='pemain_read_makan'),
]