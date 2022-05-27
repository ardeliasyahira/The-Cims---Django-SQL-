from django.shortcuts import render, HttpResponse, redirect
from utils.query import query
from home.views import get_session_data, is_authenticated, login
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def admin_read_tokoh(request):
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] == 'pemain':
        return HttpResponse("Anda bukanlah admin")
    
    print(request.POST.get("Nama"))
    if request.POST.get("NamaTokoh") != None:
        request.session['NamaTokoh'] = request.POST.get('NamaTokoh')
        return redirect('/tokoh/admin_detail_tokoh')

    # if request.POST.get("Nama") != None:
    #     request.session['Nama'] = request.POST.get('Nama')
    #     return redirect('/tokoh/pemain_update_tokoh')

    list_tokoh = query("SELECT * FROM tokoh")

    data = get_session_data(request)
    data['list_tokoh'] = list_tokoh
    print(data["list_tokoh"])

    return render(request, 'admin_read_tokoh.html', data)

def pemain_read_tokoh(request):
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] == 'admin':
        return HttpResponse('Anda bukanlah pemain')

    print(request.POST.get("Nama"))
    if request.POST.get("NamaTokoh") != None:
        request.session['NamaTokoh'] = request.POST.get('NamaTokoh')
        return redirect('/tokoh/pemain_detail_tokoh')

    # if request.POST.get("Nama") != None:
    #     request.session['Nama'] = request.POST.get('Nama')
    #     return redirect('/tokoh/pemain_update_tokoh')

    username = request.session['username']
    list_tokoh_pemain = query(f"SELECT * FROM tokoh WHERE username_pengguna = '{username}'")

    data = get_session_data(request)
    data['list_tokoh'] = list_tokoh_pemain

    print(data)

    return render(request, 'pemain_read_tokoh.html', data)

@csrf_exempt
def pemain_create_tokoh(request):
    if not is_authenticated(request):
        return login(request)
    if request.session['role'] == 'admin':
        return HttpResponse("Anda bukanlah pemain")

    username = request.session['username']
    list_warna_kulit = query("SELECT kode FROM WARNA_KULIT")
    list_pekerjaan = query("SELECT nama FROM PEKERJAAN")

    print('ngetest 1')
    print(list_warna_kulit)
    print('ngetest 2')
    print(list_pekerjaan)

    data = get_session_data(request)
    data['list_warna_kulit'] = list_warna_kulit
    data['list_pekerjaan'] = list_pekerjaan
    if request.method == 'POST':
        nama_tokoh = request.POST.get('namaTokoh')
        jenis_kelamin = request.POST.get('jenisKelamin')
        warna_kulit = request.POST.get('warnaKulit')
        pekerjaan = request.POST.get('pekerjaan')
        if nama_tokoh == '':
            pass
        else:
            query(f"""INSERT INTO TOKOH VALUES('{username}','{nama_tokoh}','{jenis_kelamin}','Aktif',
            0,100,0,0,'{warna_kulit}',1,'Jenius','{pekerjaan}','RB001','MT001','RM001'
            )""")
            return redirect("/tokoh/pemain_read_tokoh")
    return render(request,'create_tokoh.html', data)
    

def admin_detail_tokoh(request):
    if is_authenticated(request):
        print("terotentikasi")

        nama_tokoh = request.session.get('NamaTokoh')
        print(nama_tokoh)
        data_query = query(f"SELECT * FROM tokoh WHERE nama LIKE '%{nama_tokoh}%'")
        data = get_session_data(request)
        print(data_query)
        data["list"] = [data_query]
        print(data)

        return render(request, "detail_tokoh.html", data)
    else:
        print("tidak terotentikasi")
        return login(request)

def pemain_detail_tokoh(request):
    if is_authenticated(request):
        print("terotentikasi")

        nama_tokoh = request.session.get('NamaTokoh')
        print(nama_tokoh)
        username = request.session.get("username")
        data_query = query(f"SELECT * FROM tokoh WHERE  username_pengguna ='{username}' AND nama LIKE '%{nama_tokoh}%'")
        data = get_session_data(request)
        data["list"] = [data_query]
        print(data_query)
        print(data)

        return render(request, "detail_tokoh.html", data)
    else:
        print("tidak terotentikasi")
        return login(request)

@csrf_exempt
def pemain_update_tokoh(request, nama) :
    # if is_authenticated(request):
    #     print("terotentikasi")

    #     username = request.session.get("Username")
    if not is_authenticated(request):
        return login(request)
    if request.session['role'] == 'admin':
        return HttpResponse("Anda bukanlah pemain")

    username = request.session['username']
    list_tokoh = query(f"SELECT * FROM TOKOH WHERE  username_pengguna ='{username}' AND nama LIKE '%{nama}%'")

    list_rambut = query(f"""SELECT * FROM KOLEKSI_TOKOH
    WHERE username_pengguna = '{username}'
    AND nama_tokoh = '{nama}'
    AND id_koleksi LIKE 'RB%'""")

    list_mata = query(f"""SELECT * FROM KOLEKSI_TOKOH
    WHERE username_pengguna = '{username}'
    AND nama_tokoh = '{nama}'
    AND id_koleksi LIKE 'MT%'""")

    list_rumah = query(f"""SELECT * FROM KOLEKSI_TOKOH
    WHERE username_pengguna = '{username}'
    AND nama_tokoh = '{nama}'
    AND id_koleksi LIKE 'RM%'""")
    
    data = get_session_data(request)
    data["list_tokoh"] = list_tokoh
    data["list_rambut"] = list_rambut
    data["list_mata"] = list_mata
    data["list_rumah"] = list_rumah

    print(list_tokoh)
    print(len(list_rambut))
    print(list_mata)
    print(list_rumah)

    if request.method == "POST":
        data = request.POST
        id_rambut = data.get('idRambut')
        id_mata = data.get('idMata')
        id_rumah = data.get('idRumah')

        print(username)
        print(nama)
        print(id_rambut)
        print(id_mata)
        print(id_rumah)

        query(f"""
        UPDATE TOKOH
        SET id_rambut = '{id_rambut}', id_mata = '{id_mata}', id_rumah = '{id_rumah}'
        WHERE username_pengguna = '{username}'
        AND nama = '{nama}';
        """)
        return redirect("/tokoh/pemain_read_tokoh")

    return render(request,'pemain_update_tokoh.html', data)
    #     return render(request, "pemain_update_tokoh.html", data)
    # else:
    #     print("tidak terotentikasi")
    #     return login(request)