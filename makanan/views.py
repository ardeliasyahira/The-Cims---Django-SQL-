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
    list_makanan = query(f"SELECT * FROM MAKAN WHERE username_pengguna = '{username}'")
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