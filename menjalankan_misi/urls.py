from django.urls import path

from . import views

app_name = 'menjalankanmisi'

urlpatterns = [
    path('', views.login, name='login'),
    path('admin_read_menjalankan_misiutama/', views.admin_read_menjalankan_misiutama, name='admin_read_menjalankan_misiutama'),
    path('pemain_read_menjalankan_misiutama/', views.pemain_read_menjalankan_misiutama, name='pemain_read_menjalankan_misiutama'),
    path('pemain_create_menjalankan_misiutama/', views.pemain_create_menjalankan_misiutama, name='pemain_create_menjalankan_misiutama'),
    path('pemain_update_menjalankan_misiutama/<str:namatokoh>/<str:namamisi>', views.pemain_update_menjalankan_misiutama, name='pemain_update_menjalankan_misiutama'),
]