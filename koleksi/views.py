from django.shortcuts import render, HttpResponse
from utils.query import query
from database.views import get_session_data, is_authenticated, login
from django.views.decorators.csrf import csrf_exempt

def admin_read_koleksi(request):
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] == 'pemain':
        return HttpResponse("Anda bukanlah admin")
    
    list_koleksi = query("SELECT * FROM koleksi")

    data = get_session_data(request)
    data['list_koleksi'] = list_koleksi


    return render(request, 'admin_read_koleksi.html', data)

def pemain_read_koleksi(request):
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] == 'admin':
        return HttpResponse("Anda bukanlah pemain")
    
    list_koleksi = query("SELECT * FROM koleksi")

    data = get_session_data(request)
    data['list_koleksi'] = list_koleksi


    return render(request, 'pemain_read_koleksi.html', data)

@csrf_exempt
def create_koleksi(request):
    if not is_authenticated(request):
        return login(request)
    
    if str(request.session['role']) == 'pemain':
        return HttpResponse("You are not authorized")
    
    if request.method != 'POST':
        return create_koleksi_view(request)
    
    body = request.POST
    id_koleksi = str(body.get('id_koleksi_input'))
    harga = str(body.get('harga_input'))

    result = query(
        f"""
        INSERT INTO koleksi VALUES
        ( '{id_koleksi}', '{harga}')
    """
    )

    if not type(result) == int:
        return HttpResponse("Gagal Memasukkan Data")
    
    return admin_read_koleksi(request)


def create_koleksi_view(request):
    data = {}
    
    koleksi = query(
        "SELECT * FROM koleksi"
    )

    data['koleksi'] = koleksi

    return render(request, 'create_koleksi.html', data)


@csrf_exempt
def delete_koleksi(request):
    if not is_authenticated(request):
        return login(request)
    
    if str(request.session['role']) == 'pemain':
        return HttpResponse("You are not authorized")
    
    if request.method != 'POST':
        return delete_koleksi_view(request)
    
    body = request.POST
    id_koleksi = str(body.get('id_koleksi_input'))

    result = query(
        f"""
        DELETE FROM koleksi WHERE
        ( id_koleksi = '{id_koleksi}')
    """
    )

    if not type(result) == int:
        return HttpResponse("Gagal Menghapus Data")
    
    return admin_read_koleksi(request)


def delete_koleksi_view(request):
    data = {}
    
    koleksi = query(
        "SELECT * FROM koleksi"
    )

    data['koleksi'] = koleksi

    return render(request, 'delete_koleksi.html', data)

@csrf_exempt
def update_koleksi(request):
    if not is_authenticated(request):
        return login(request)
    
    if str(request.session['role']) == 'pemain':
        return HttpResponse("You are not authorized")
    
    if request.method != 'POST':
        return update_koleksi_view(request)
    
    body = request.POST
    id_koleksi = str(body.get('id_koleksi_input'))
    harga = str(body.get('harga_input'))

    result = query(
        f"""
        INSERT INTO level VALUES
        ( '{id_koleksi}', '{harga}')
    """
    )

    if not type(result) == int:
        return HttpResponse("Gagal Memasukkan Data")
    
    return admin_read_koleksi(request)


def update_koleksi_view(request):
    data = {}
    
    koleksi = query(
        "SELECT * FROM koleksi"
    )

    data['koleksi'] = koleksi

    return render(request, 'update_koleksi.html', data)
