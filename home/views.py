from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from database.views import is_authenticated, get_session_data, login, login_view

# Create your views here.

def admin_homepage(request):
    if is_authenticated(request):
        if request.session['role'] != 'admin':
            return HttpResponse("Anda bukanlah seorang admin :'D")
        return render(request, "admin_homepage.html", get_session_data(request))
    else:
        return login(request)

def pemain_homepage(request):
    if is_authenticated(request):
        if request.session['role'] != 'pemain':
            return HttpResponse("Anda pemain")
        return render(request, "pemain_homepage.html", get_session_data(request))
    else:
        return login(request)
