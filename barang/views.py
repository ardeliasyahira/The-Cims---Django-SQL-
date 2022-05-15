from django.shortcuts import render, HttpResponse
from utils.query import query
from home.views import get_session_data, is_authenticated, login

def admin_read_barang(request):
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] == 'pemain':
        return HttpResponse("Anda bukanlah admin")
    
    list_menggunakan_barang = query("""
    SELECT * 
    FROM MENGGUNAKAN_BARANG MB, KOLEKSI_JUAL_BELI KJ
    WHERE MB.id_barang = KJ.id_koleksi
    """)

    data = get_session_data(request)
    data['list_menggunakan_barang'] = list_menggunakan_barang

    return render(request, 'admin_read_barang.html', data)

def pemain_read_barang(request):
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] == 'admin':
        return HttpResponse("Anda bukanlah pemain")

    username = request.session['username']
    list_menggunakan_barang = query(f"""
    SELECT nama_tokoh, nama, waktu
    FROM menggunakan_barang, koleksi_jual_beli 
    WHERE username_pengguna = '{username}' AND menggunakan_barang.id_barang = koleksi_jual_beli.id_koleksi
    """)

    data = get_session_data(request)
    data['list_menggunakan_barang'] = list_menggunakan_barang

    return render(request, 'pemain_read_barang.html', data)

def pemain_create_barang(request) :
    return render(request, 'pemain_create_barang.html')
