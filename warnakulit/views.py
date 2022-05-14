from django.shortcuts import render, HttpResponse
from utils.query import query
from database.views import get_session_data, is_authenticated, login

def admin_read_warna_kulit(request):
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] == 'pemain':
        return HttpResponse("Anda haruslah seorang admin")

    list_warna_kulit = query("SELECT * FROM warna_kulit")
    print(list_warna_kulit)
    data = get_session_data(request)
    data['list_warna_kulit'] = list_warna_kulit
    data['idx'] = 0
    print(data['list_warna_kulit'])

    return render(request, 'admin_read_warna_kulit.html', data)

def pemain_read_warna_kulit(request):
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] == 'admin':
        return HttpResponse("Anda haruslah seorang pemain")

    list_warna_kulit = query("SELECT * FROM warna_kulit")

    data = get_session_data(request)
    data['list_warna_kulit'] = list_warna_kulit
    data['idx'] = 0
    
    return render(request, "pemain_read_warna_kulit.html", data)

