from django.shortcuts import render, HttpResponse
from utils.query import query
from home.views import get_session_data, is_authenticated, login

# Create your views here.
def read_pekerjaan(request):
    if not is_authenticated(request):
        return login(request)
    
    list_pekerjaan = query("SELECT * FROM PEKERJAAN")

    data = get_session_data(request)
    data['list_pekerjaan'] = list_pekerjaan

    if request.session['role'] == "admin":
        return render(request, 'admin_read_pekerjaan.html', data)
    else:
        return render(request, 'pemain_read_pekerjaan.html', data)

def read_bekerja(request):
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] == "admin":
        list_bekerja = query("SELECT * FROM BEKERJA")
        data = get_session_data(request)
        data['list_bekerja'] = list_bekerja
        
        return render(request, "admin_read_bekerja.html", data)
        
    if request.session['role'] == "pemain":
        username = request.session['username']
        list_bekerja = query(f"SELECT * FROM BEKERJA WHERE username_pengguna = '{username}'")
        data = get_session_data(request)
        data['list_bekerja'] = list_bekerja
        
        return render(request, "pemain_read_bekerja.html", data)

def admin_create_pekerjaan(request) :
    return render(request, 'admin_create_pekerjaan.html')

def admin_update_pekerjaan(request) :
    return render(request, 'admin_update_pekerjaan.html')
