from django.urls import path

from . import views

app_name = 'pekerjaan'

urlpatterns = [
    path('read_pekerjaan', views.read_pekerjaan, name='read_pekerjaan'),
    path('read_bekerja', views.read_bekerja, name="read_bekerja"),
    path('admin_create_pekerjaan/', views.admin_create_pekerjaan, name='admin_create_pekerjaan'),
    path('admin_update_pekerjaan/', views.admin_update_pekerjaan, name='admin_update_pekerjaan'),
]
