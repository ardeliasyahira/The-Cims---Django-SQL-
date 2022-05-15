from django.urls import path

from . import views

app_name = 'misiutama'

urlpatterns = [
    path('', views.login, name='login'),
    path('admin_read_misiutama/', views.admin_read_misiutama, name='admin_read_misiutama'),
    path('admin_detail_misiutama/<str:nama>', views.admin_detail_misiutama, name='admin_detail_misiutama'),
    path('pemain_read_misiutama/', views.pemain_read_misiutama, name='pemain_read_misiutama'),
    path('pemain_detail_misiutama/<str:nama>', views.pemain_detail_misiutama, name='pemain_detail_misiutama'),
]