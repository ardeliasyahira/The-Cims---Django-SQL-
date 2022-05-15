from django.shortcuts import render, HttpResponse
from utils.query import query
from database.views import get_session_data, is_authenticated, login
from django.views.decorators.csrf import csrf_exempt

def admin_read_koleksitokoh(request):
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] == 'pemain':
        return HttpResponse("Anda bukanlah admin")
    
    list_koleksi_tokoh = query("SELECT * FROM koleksi_tokoh")

    data = get_session_data(request)
    data['list_koleksi_tokoh'] = list_koleksi_tokoh


    return render(request, 'admin_read_koleksi_tokoh.html', data)

def pemain_read_koleksi_tokoh(request):
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] == 'admin':
        return HttpResponse("Anda bukanlah pemain")
    
    list_koleksi_tokoh = query("SELECT * FROM koleksi_tokoh")

    data = get_session_data(request)
    data['list_koleksi_tokoh'] = list_koleksi_tokoh


    return render(request, 'pemain_read_koleksi_tokoh.html', data)

@csrf_exempt
def create_koleksi_tokoh(request):
    if not is_authenticated(request):
        return login(request)
    
    if str(request.session['role']) == 'pemain':
        return HttpResponse("You are not authorized")
    
    if request.method != 'POST':
        return create_koleksi_tokoh_view(request)
    
    body = request.POST
    id_koleksi = str(body.get('id_koleksi_input'))
    username_pengguna = str(body.get('username_pengguna_input'))
    nama_tokoh = str(body.get('nama_tokoh_input'))

    result = query(
        f"""
        INSERT INTO kategori_apparel VALUES
        ( '{id_koleksi}', '{username_pengguna}', '{nama_tokoh}')
    """
    )

    if not type(result) == int:
        return HttpResponse("Gagal Memasukkan Data")
    
    return admin_read_koleksitokoh(request)


def create_koleksi_tokoh_view(request):
    data = {}
    
    koleksi_tokoh = query(
        "SELECT * FROM koleksi_tokoh"
    )

    data['koleksi_tokoh'] = koleksi_tokoh

    return render(request, 'create_koleksi_tokoh.html', data)


@csrf_exempt
def delete_koleksi_tokoh(request):
    if not is_authenticated(request):
        return login(request)
    
    if str(request.session['role']) == 'pemain':
        return HttpResponse("You are not authorized")
    
    if request.method != 'POST':
        return delete_koleksi_tokoh_view(request)
    
    body = request.POST
    id_koleksi = str(body.get('id_koleksi_input'))
    username_pengguna = str(body.get('username_pengguna_input'))
    nama_tokoh = str(body.get('nama_tokoh_input'))

    result = query(
        f"""
        DELETE FROM koleksi_tokoh WHERE
        ( id_koleksi = '{id_koleksi}' AND username_pengguna = '{username_pengguna}' AND nama_tokoh = '{nama_tokoh}')
    """
    )

    if not type(result) == int:
        return HttpResponse("Gagal Menghapus Data")
    
    return admin_read_koleksitokoh(request)


def delete_koleksi_tokoh_view(request):
    data = {}
    
    koleksi_tokoh = query(
        "SELECT * FROM koleksi_tokoh"
    )

    data['koleksi_tokoh'] = koleksi_tokoh

    return render(request, 'delete_koleksi_tokoh.html', data)