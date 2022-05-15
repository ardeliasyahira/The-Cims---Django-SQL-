from django.shortcuts import render, HttpResponse
from utils.query import query
from database.views import get_session_data, is_authenticated, login
from django.views.decorators.csrf import csrf_exempt

def admin_read_warna_kulit(request):
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] == 'pemain':
        return HttpResponse("Anda haruslah seorang admin")

    list_warna_kulit = query("SELECT * FROM warna_kulit")
    
    data = get_session_data(request)
    data['list_warna_kulit'] = list_warna_kulit
    data['idx'] = 0

    return render(request, 'admin_read_warna_kulit.html', data)

def pemain_read_warna_kulit(request):
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] == 'admin':
        return HttpResponse("Anda haruslah seorang pemain")

    list_warna_kulit = query("SELECT * FROM warna_kulit")

    data = get_session_data(request)
    data['list_warna_kulit'] = list_warna_kulit
    data['idx'] = 0
    
    return render(request, "pemain_read_warna_kulit.html", data)

@csrf_exempt
def create_warnakulit(request):
    if not is_authenticated(request):
        return login(request)
    
    if str(request.session['role']) == 'pemain':
        return HttpResponse("You are not authorized")
    
    if request.method != 'POST':
        return create_warnakulit_view(request)
    
    body = request.POST
    warna_kulit     = str(body.get('kode_input'))

    result = query(
        f"""
        INSERT INTO warna_kulit VALUES
        ( '{warna_kulit}')
    """
    )

    print(result)

    if not type(result) == int:
        return HttpResponse("Gagal Memasukkan Data")
    
    return admin_read_warna_kulit(request)


def create_warnakulit_view(request):
    data = {}
    
    kode_warna_kulit = query(
        "SELECT * FROM warna_kulit"
    )

    data['kode_warna_kulit'] = kode_warna_kulit

    return render(request, 'create_warna_kulit.html', data)


