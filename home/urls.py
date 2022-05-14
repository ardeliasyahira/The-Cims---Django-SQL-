from django.urls import path 
from .views import admin_homepage, pemain_homepage

urlpatterns = [
    path('admin_homepage/', admin_homepage, name='admin_homepage'),
    path('pemain_homepage/', pemain_homepage, name='pemain_homepage'),
    
]
