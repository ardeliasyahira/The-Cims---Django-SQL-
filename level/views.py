from django.shortcuts import render, HttpResponse
from utils.query import query
from database.views import get_session_data, is_authenticated, login

def admin_read_level(request):
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] == 'pemain':
        return HttpResponse("Anda bukanlah admin")
    
    list_level = query("SELECT * FROM level")

    data = get_session_data(request)
    data['list_level'] = list_level

    print(data)

    return render(request, 'admin_read_level.html', data)

def pemain_read_level(request):
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] == 'admin':
        return HttpResponse("Anda bukanlah pemain")
    
    list_level = query("SELECT * FROM level")

    data = get_session_data(request)
    data['list_level'] = list_level

    print(data)

    return render(request, 'pemain_read_level.html', data)