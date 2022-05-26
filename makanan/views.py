from django.shortcuts import render, HttpResponse, redirect
from utils.query import query
from home.views import get_session_data, is_authenticated, login
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def admin_read_makanan(request):
    if not is_authenticated(request):
        return login(request)
    if request.session['role'] == 'pemain':
        return HttpResponse("Anda bukanlah admin")

    list_makanan = query("SELECT * FROM MAKANAN")
    print(list_makanan)
    
    list_makanan_dimakan = query("SELECT DISTINCT nama_makanan FROM MAKAN")

    list_list_makanan_dimakan = []

    for i in list_makanan_dimakan:
        list_list_makanan_dimakan.append(i['nama_makanan'])

    print(list_list_makanan_dimakan)

    for i in list_makanan:
        i['ada'] = False

    print(list_makanan)

    for i in list_makanan:
        if i['nama'] in list_list_makanan_dimakan:
            i['ada'] = True

    print("ngetes")
    print(list_makanan)

    data = get_session_data(request)
    data['list_makanan'] = list_makanan

    return render(request, 'admin_read_makanan.html', data)

def pemain_read_makanan(request):
    if not is_authenticated(request):
        return login(request)
    if request.session['role'] == 'admin':
        return HttpResponse("Anda bukanlah pemain")

    username = request.session['username']
    list_makanan = query("SELECT * FROM MAKANAN")
    print("ngetest")
    print(list_makanan)

    data = get_session_data(request)
    data['list_makanan'] = list_makanan

    return render(request, 'pemain_read_makanan.html', data)

@csrf_exempt
def admin_create_makanan(request):
    if not is_authenticated(request):
        return login(request)
    if request.session['role'] == 'pemain':
        return HttpResponse("Anda bukanlah admin")

    if request.method == "POST":
        data = request.POST
        nama = data.get('namaMakanan')
        harga = data.get('hargaMakanan')
        tingkat_energi = data.get('tingkatEnergi')
        tingkat_kelaparan = data.get('tingkatKelaparan')

        query(f"INSERT INTO MAKANAN VALUES('{nama}',{harga},{tingkat_energi},{tingkat_kelaparan})")
        return redirect("/makanan/admin_read_makanan/")
    return render(request, 'admin_create_makanan.html')

def admin_delete_makanan(request, nama):
    if not is_authenticated(request):
        return login(request)
    if request.session['role'] == 'pemain':
        return HttpResponse("Anda bukanlah admin")
    
    print(nama)
    query(f"DELETE FROM MAKANAN WHERE nama = '{nama}'")
    return redirect("/makanan/admin_read_makanan/")

@csrf_exempt
def admin_update_makanan(request, nama):
    if not is_authenticated(request):
        return login(request)
    if request.session['role'] == 'pemain':
        return HttpResponse("Anda bukanlah admin")

    list_makanan = query(f"SELECT * FROM MAKANAN WHERE nama = '{nama}'")
    print("ngetest")
    print(list_makanan)

    data = get_session_data(request)
    data['list_makanan'] = list_makanan

    if request.method == "POST":
        data = request.POST
        nama = list_makanan.get('nama')
        harga = data.get('hargaMakanan')
        tingkat_energi = data.get('tingkatEnergi')
        tingkat_kelaparan = data.get('tingkatKelaparan')

        print(nama)
        print(harga)
        print(tingkat_energi)
        print(tingkat_kelaparan)

        query(f"""
        UPDATE MAKANAN
        SET harga = {harga}, tingkat_energi = {tingkat_energi}, tingkat_kelaparan = {tingkat_kelaparan}
        WHERE nama = '{nama}';
        """)
        return redirect("/makanan/admin_read_makanan/")

    return render(request,'admin_update_makanan.html', data)