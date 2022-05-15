from django.urls import path 
from .views import login, register, index, register_admin, register_pemain, logout

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
]
