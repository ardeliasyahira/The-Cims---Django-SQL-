from django.urls import path

from . import views

app_name = 'tokoh'

urlpatterns = [
    path('admin_read_tokoh', views.admin_read_tokoh, name='admin_read_tokoh'),
    path('pemain_read_tokoh', views.pemain_read_tokoh, name='pemain_read_tokoh'),
]
