from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from database.views import is_authenticated, get_session_data, login, login_view, query

# Create your views here.

def admin_homepage(request):
    if is_authenticated(request):
        if request.session['role'] == 'admin':
            #return HttpResponse("Anda bukanlah seorang admin :'D")
            context = {}
            context['username'] = request.session['username']
        return render(request, "admin_homepage.html", context)
    else:
        return login(request)

def pemain_homepage(request):
    if is_authenticated(request):
        if request.session['role'] == 'pemain':
            #return HttpResponse("Anda pemain")
            query_pemain = query(f"SELECT username, email, no_hp, koin FROM PEMAIN WHERE username = '{request.session['username']}'")
            context={}
            context ['pemain'] = query_pemain
        return render(request, "pemain_homepage.html", context)
    else:
        return login(request)
