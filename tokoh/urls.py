from django.urls import path

from . import views

app_name = 'tokoh'

urlpatterns = [
    path('admin_read_tokoh', views.admin_read_tokoh, name='admin_read_tokoh'),
    path('pemain_read_tokoh', views.pemain_read_tokoh, name='pemain_read_tokoh'),
    path('pemain_detail_tokoh', views.pemain_detail_tokoh, name='pemain_detail_tokoh'),
    path('admin_detail_tokoh', views.admin_detail_tokoh, name='admin_detail_tokoh'),
    path('pemain_update_tokoh', views.pemain_update_tokoh, name='pemain_update_tokoh'),
]
