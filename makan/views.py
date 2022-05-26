from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from utils.query import query
from home.views import get_session_data, is_authenticated, login
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
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
    print(username)
    
    list_makan = query(f"SELECT nama_tokoh, waktu, nama_makanan FROM MAKAN WHERE username_pengguna = '{username}'")
    print("ngetest")
    print(list_makan)

    data = get_session_data(request)
    data['list_makan'] = list_makan

    return render(request, 'pemain_read_makan.html', data)

@csrf_exempt
def pemain_create_makan(request):
    if not is_authenticated(request):
        return login(request)
    if request.session['role'] == 'admin':
        return HttpResponse("Anda bukanlah pemain")

    username = request.session['username']
    
    list_tokoh = query(f"SELECT DISTINCT nama FROM TOKOH WHERE username_pengguna = '{username}'")
    
    list_makan = query("SELECT nama FROM MAKANAN ")

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

    data = get_session_data(request)
    data['list_makan'] = list_makan
    data['list_tokoh'] = list_tokoh

    print(username)
    print(now)
    print(list_tokoh)
    print(list_makan)

    if request.method == 'POST':
        nama_tokoh = request.POST.get('namaTokoh')
        nama_makanan = request.POST.get('namaMakanan')
        # query(f"INSERT INTO MAKAN VALUES('{username}','{nama_tokoh}','{now}','{nama_makanan}')")
        print(username)
        print(nama_tokoh)
        print(now)
        print(nama_makanan)
        
        query(f"INSERT INTO MAKAN VALUES('{username}','{nama_tokoh}','{now}','{nama_makanan}')")
        return HttpResponseRedirect("/makan/pemain_read_makan/")

    return render(request, 'pemain_create_makan.html', data)
