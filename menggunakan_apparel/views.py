from django.shortcuts import render, HttpResponse
from utils.query import query
from database.views import get_session_data, is_authenticated, login

def list_admin_menggunakan_apparel(request):
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] == 'pemain':
        return HttpResponse("Anda bukanlah admin")
    
    list_menggunakan_apparel = query("""
    SELECT * 
    FROM menggunakan_apparel, apparel, koleksi_jual_beli
    WHERE menggunakan_apparel.id_koleksi = apparel.id_koleksi AND menggunakan_apparel.id_koleksi = koleksi_jual_beli.id_koleksi
    """)
    print(list_menggunakan_apparel)

    data = get_session_data(request)
    data['list_menggunakan_apparel'] = list_menggunakan_apparel

    print(data)

    return render(request, 'list_admin_menggunakan_apparel.html', data)

def list_pemain_menggunakan_apparel(request):
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] == 'admin':
        return HttpResponse("Anda bukanlah pemain")
    
    username = request.session['username']
    list_menggunakan_apparel = query(f"""
    SELECT * 
    FROM menggunakan_apparel, apparel, koleksi_jual_beli
    WHERE username_pengguna = '{username}' AND menggunakan_apparel.id_koleksi = apparel.id_koleksi AND menggunakan_apparel.id_koleksi = koleksi_jual_beli.id_koleksi
    """)

    data = get_session_data(request)
    data['list_menggunakan_apparel'] = list_menggunakan_apparel

    print(data)

    return render(request, 'list_pemain_menggunakan_apparel.html', data)