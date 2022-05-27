from django.shortcuts import redirect, render, HttpResponse
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
    WHERE menggunakan_apparel.username_pengguna = '{username}' AND menggunakan_apparel.id_koleksi = apparel.id_koleksi AND menggunakan_apparel.id_koleksi = koleksi_jual_beli.id_koleksi
    """
    , True)

    data = get_session_data(request)
    data['list_menggunakan_apparel'] = list_menggunakan_apparel
    print(list_menggunakan_apparel)

    if request.method == 'POST':
        if request.POST.get("DeleteButton") != None:
            request.session['Values'] = request.POST.get('DeleteButton')
            return delete_menggunakan_apparel(request)


    return render(request, 'list_pemain_menggunakan_apparel.html', data)

def create_menggunakanapparel_view(request):
    data = {}
    if request.POST.get('nama_tokoh_input') != None:
        if request.POST.get('apparel_input') != None:
            return create_menggunakanapparel(request)

    username = request.session['username']
    nama_tokoh = query(f"""
    SELECT nama
    FROM TOKOH
    WHERE username_pengguna = '{username}'
    ORDER BY nama ASC;
    """
    , True)

    data = get_session_data(request)
    data['nama_tokoh'] = nama_tokoh

    apparel = query(f"""
    SELECT KT.id_koleksi
    FROM KOLEKSI_TOKOH KT, APPAREL A
    WHERE KT.username_pengguna = '{username}' AND KT.id_koleksi = A.id_koleksi
    ORDER BY id_koleksi ASC;
    """
    , True)

    
    data['apparel'] = apparel
    print(nama_tokoh)
    print(apparel)

    return render(request, 'create_menggunakan_apparel.html', data)

@csrf_exempt
def create_menggunakanapparel(request):
    if not is_authenticated(request):
        return login(request)
    
    if str(request.session['role']) == 'admin':
        return HttpResponse("You are not authorized")
    
    
    body = request.POST
    username = request.session['username']
    nama_tokoh = str(body.get('nama_tokoh_input'))
    apparel = str(body.get('apparel_input'))
    result = query(
        f"""
        INSERT INTO MENGGUNAKAN_APPAREL VALUES
        ( '{username}', '{nama_tokoh}', '{apparel}')
    """
    )

    
    return redirect('/menggunakan_apparel/pemain/list_menggunakan_apparel')


def delete_menggunakan_apparel(request):
    if not is_authenticated(request):
        return login(request)
    
    if request.session['role'] == 'admin':
        return HttpResponse("Anda bukanlah pemain")

    values = request.session.get("Values")
    values_list = values.split(", ")

    username_pengguna = values_list[0]
    nama_tokoh = values_list[1]
    id_koleksi = values_list[2]
    delete_query = query(f"""
        DELETE FROM MENGGUNAKAN_APPAREL
        WHERE username_pengguna = '{username_pengguna}'
        AND nama_tokoh = '{nama_tokoh}'
        AND id_koleksi = '{id_koleksi}'
    """)

    return redirect('/menggunakan_apparel/pemain/list_menggunakan_apparel')
