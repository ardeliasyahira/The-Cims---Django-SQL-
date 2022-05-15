"""thecims URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import database.urls as database
import home.urls as home
import tokoh.urls as tokoh
import barang.urls as barang
import pekerjaan.urls as pekerjaan
import misiutama.urls as misiutama
import warnakulit.urls as warnakulit
import tokoh.urls as tokoh
import level.urls as level
import menggunakan_apparel.urls as apparel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(database)),
    path('home/', include(home)),
    path('warnakulit/', include(warnakulit)),
    path('tokoh/', include(tokoh)),
    path('barang/', include(barang)),
    path('pekerjaan/', include(pekerjaan)),
    path('misi_utama/', include(misiutama)),
    path('tokoh/', include(tokoh)),
    path('level/', include(level)),
    path('menggunakan_apparel/', include(apparel))
]

