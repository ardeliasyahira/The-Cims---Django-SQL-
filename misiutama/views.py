from django.shortcuts import render, HttpResponse
from utils.query import query
from home.views import get_session_data, is_authenticated, login
# Create your views here.

def admin_read_misiutama(request):
    if not is_authenticated(request):
        return login(request)
    if request.session['role'] == 'pemain':
        return HttpResponse("Anda bukanlah admin")

    list_misiutama = query("SELECT * FROM MISI_UTAMA")

    data = get_session_data(request)
    data['list_misiutama'] = list_misiutama

    return render(request, 'admin_read_misiutama.html', data)

def pemain_read_misiutama(request):
    if not is_authenticated(request):
        return login(request)
    if request.session['role'] == 'admin':
        return HttpResponse("Anda bukanlah pemain")

    list_misiutama = query("SELECT * FROM MISI_UTAMA")

    data = get_session_data(request)
    data['list_misiutama'] = list_misiutama

    return render(request, 'pemain_read_misiutama.html', data)

def pemain_detail_misiutama(request, nama):
    if not is_authenticated(request):
        return login(request)
    if request.session['role'] == 'admin':
        return HttpResponse("Anda bukanlah pemain")

    list_detailmisi = query(f"SELECT * FROM MISI WHERE nama = '{nama}'")
    print(list_detailmisi)


    data = get_session_data(request)
    data['list_detailmisi'] = list_detailmisi

    return render(request, 'detail_read_misiutama.html', data)

def admin_detail_misiutama(request, nama):
    if not is_authenticated(request):
        return login(request)
    if request.session['role'] == 'pemain':
        return HttpResponse("Anda bukanlah admin")

    list_detailmisi = query(f"SELECT * FROM MISI WHERE nama = '{nama}'")
    print(list_detailmisi)

    data = get_session_data(request)
    data['list_detailmisi'] = list_detailmisi

    return render(request, 'detail_read_misiutama.html', data)
