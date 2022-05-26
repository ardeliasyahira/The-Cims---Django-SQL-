from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from utils.query import query
from home.views import get_session_data, is_authenticated, login
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def admin_read_menjalankan_misiutama(request):
    if not is_authenticated(request):
        return login(request)
    if request.session['role'] == 'pemain':
        return HttpResponse("Anda bukanlah admin")

    list_menjalankan_misiutama = query("SELECT * FROM MENJALANKAN_MISI_UTAMA")
    print('ngetest 1')
    print(list_menjalankan_misiutama)
    print('ngetest 2')
    
    data = get_session_data(request)
    data['list_menjalankan_misiutama'] = list_menjalankan_misiutama

    return render(request, 'admin_read_menjalankan_misiutama.html', data)

def pemain_read_menjalankan_misiutama(request):
    if not is_authenticated(request):
        return login(request)
    if request.session['role'] == 'admin':
        return HttpResponse("Anda bukanlah pemain")

    username = request.session['username']

    # list_menjalankan_misiutama = query("""SELECT nama_tokoh, mama_misi, status 
    # FROM MENJALANKAN_MISI_UTAMA
    # WHERE username_pengguna = '{username}' """)

    list_menjalankanmisi = query(f"SELECT nama_tokoh, nama_misi, status FROM MENJALANKAN_MISI_UTAMA WHERE username_pengguna = '{username}'")

    print('ngetest 1')
    print(list_menjalankanmisi)
    print('ngetest 2')
    
    data = get_session_data(request)
    data['list_menjalankanmisi'] = list_menjalankanmisi

    return render(request, 'pemain_read_menjalankan_misiutama.html', data)


@csrf_exempt
def pemain_create_menjalankan_misiutama(request):
    if not is_authenticated(request):
        return login(request)
    if request.session['role'] == 'admin':
        return HttpResponse("Anda bukanlah pemain")

    username = request.session['username']
    list_tokoh = query(f"SELECT DISTINCT nama FROM TOKOH WHERE username_pengguna = '{username}'")
    list_misi = query("SELECT nama_misi FROM MISI_UTAMA ")

    data = get_session_data(request)
    data['list_misi'] = list_misi
    data['list_tokoh'] = list_tokoh

    print(username)
    print(list_tokoh)
    print(list_misi)

    if request.method == 'POST':
        nama_tokoh = request.POST.get('namaTokoh')
        nama_misi = request.POST.get('namaMisi')
        print(username)
        print(nama_tokoh)
        print(nama_misi)
        
        query(f"INSERT INTO MENJALANKAN_MISI_UTAMA VALUES('{username}','{nama_tokoh}','{nama_misi}','In Progress')")
        return HttpResponseRedirect("/menjalankan_misi/pemain_read_menjalankan_misiutama/")

    return render(request, 'pemain_create_menjalankan_misiutama.html', data)

@csrf_exempt
def pemain_update_menjalankan_misiutama(request, namatokoh, namamisi):
    if not is_authenticated(request):
        return login(request)
    if request.session['role'] == 'admin':
        return HttpResponse("Anda bukanlah pemain")

    username = request.session['username']

    list_menjalankanmisi = query(f"SELECT nama_tokoh, nama_misi, status FROM MENJALANKAN_MISI_UTAMA WHERE nama_tokoh = '{namatokoh}' AND nama_misi = '{namamisi}'")

    print('ngetest 1')
    print(list_menjalankanmisi)

    data = get_session_data(request)
    data['list_menjalankanmisi'] = list_menjalankanmisi

    if request.method == "POST":
        data = request.POST
        nama_tokoh = namatokoh
        nama_misi = list_menjalankanmisi.get('nama_misi')
        status = data.get('status')

        print(nama_tokoh)
        print(nama_misi)
        print(status)

        query(f"""
        UPDATE MENJALANKAN_MISI_UTAMA
        SET status = '{status}'
        WHERE username_pengguna = '{username}'
        AND nama_tokoh = '{nama_tokoh}'
        AND nama_misi = '{nama_misi}';
        """)
        return HttpResponseRedirect("/menjalankan_misi/pemain_read_menjalankan_misiutama/")

    return render(request,'pemain_update_menjalankan_misiutama.html', data)