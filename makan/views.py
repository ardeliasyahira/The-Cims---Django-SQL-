from django.shortcuts import render, HttpResponse
from utils.query import query
from home.views import get_session_data, is_authenticated, login
# Create your views here.

def admin_read_makan(request):
    if not is_authenticated(request):
        return login(request)
    if request.session['role'] == 'pemain':
        return HttpResponse("Anda bukanlah admin")

    list_makan = query("SELECT * FROM MAKAN")

    data = get_session_data(request)
    data['list_makan'] = list_makan

    return render(request, 'admin_read_makan.html', data)

def pemain_read_makan(request):
    if not is_authenticated(request):
        return login(request)
    if request.session['role'] == 'admin':
        return HttpResponse("Anda bukanlah pemain")

    username = request.session['username']
    list_makan = query(f"SELECT nama_tokoh, waktu, nama_makanan FROM MAKAN WHERE username_pengguna = '{username}'")
    print("ngetest")
    print(list_makan)

    data = get_session_data(request)
    data['list_makan'] = list_makan

    return render(request, 'pemain_read_makan.html', data)