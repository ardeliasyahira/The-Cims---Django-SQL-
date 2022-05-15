from django.shortcuts import render, HttpResponse
from utils.query import query
from database.views import get_session_data, is_authenticated, login
from django.views.decorators.csrf import csrf_exempt

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

    data = get_session_data(request)
    data['list_menggunakan_apparel'] = list_menggunakan_apparel


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


    return render(request, 'list_pemain_menggunakan_apparel.html', data)

@csrf_exempt
def create_menggunakanapparel(request):
    if not is_authenticated(request):
        return login(request)
    
    if str(request.session['role']) == 'admin':
        return HttpResponse("You are not authorized")
    
    if request.method != 'POST':
        return create_menggunakanapparel_view(request)
    
    body = request.POST
    nama_tokoh = str(body.get('nama_tokoh_input'))
    apparel = str(body.get('apparel_input'))

    result = query(
        f"""
        INSERT INTO level VALUES
        ( '{nama_tokoh}', '{apparel}')
    """
    )


    if not type(result) == int:
        return HttpResponse("Gagal Memasukkan Data")
    
    return list_pemain_menggunakan_apparel(request)


def create_menggunakanapparel_view(request):
    data = {}
    
    nama_tokoh = query(
        "SELECT * FROM tokoh"
    )

    data['nama_tokoh'] = nama_tokoh

    apparel = query(
        "SELECT * FROM koleksi_tokoh"
    )

    data['apparel'] = apparel

    return render(request, 'create_menggunakan_apparel.html', data)