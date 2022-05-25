from django.shortcuts import render, HttpResponse
from utils.query import query
from database.views import get_session_data, is_authenticated, login
from django.views.decorators.csrf import csrf_exempt

def admin_read_kategoriapparel(request):
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] == 'pemain':
        return HttpResponse("Anda bukanlah admin")
    
    list_kategori_apparel = query("SELECT * FROM kategori_apparel")

    data = get_session_data(request)
    data['list_kategori_apparel'] = list_kategori_apparel


    return render(request, 'admin_read_kategori_apparel.html', data)

def pemain_read_kategoriapparel(request):
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] == 'admin':
        return HttpResponse("Anda bukanlah pemain")
    
    list_kategori_apparel = query("SELECT * FROM kategori_apparel")

    data = get_session_data(request)
    data['list_kategori_apparel'] = list_kategori_apparel


    return render(request, 'pemain_read_kategori_apparel.html', data)

@csrf_exempt
def create_kategori_apparel(request):
    if not is_authenticated(request):
        return login(request)
    
    if str(request.session['role']) == 'pemain':
        return HttpResponse("You are not authorized")
    
    if request.method != 'POST':
        return create_kategori_apparel_view(request)
    
    body = request.POST
    nama_kategori = str(body.get('nama_kategori_input'))

    result = query(
        f"""
        INSERT INTO kategori_apparel VALUES
        ( '{nama_kategori}')
    """
    )

    if not type(result) == int:
        return HttpResponse("Gagal Memasukkan Data")
    
    return admin_read_kategoriapparel(request)


def create_kategori_apparel_view(request):
    data = {}
    
    kategori_apparel = query(
        "SELECT * FROM kategori_apparel"
    )

    data['kategori_apparel'] = kategori_apparel

    return render(request, 'create_kategori_apparel.html', data)


@csrf_exempt
def delete_kategori_apparel(request):
    if not is_authenticated(request):
        return login(request)
    
    if str(request.session['role']) == 'pemain':
        return HttpResponse("You are not authorized")
    
    if request.method != 'POST':
        return delete_kategori_apparel_view(request)
    
    body = request.POST
    nama_kategori = str(body.get('nama_kategori_input'))

    result = query(
        f"""
        DELETE FROM kategori_apparel WHERE
        ( 'nama_kategori' = '{nama_kategori}')
    """
    )

    if not type(result) == int:
        return HttpResponse("Gagal Menghapus Data")
    
    return admin_read_kategoriapparel(request)


def delete_kategori_apparel_view(request):
    data = {}
    
    kategori_apparel = query(
        "SELECT * FROM kategori_apparel"
    )

    data['kategori_apparel'] = kategori_apparel

    return render(request, 'delete_kategori_apparel.html', data)