from django.shortcuts import render, HttpResponse
from utils.query import query
from home.views import get_session_data, is_authenticated, login

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

    list_menjalankan_misiutama = query("SELECT MMU.Nama_tokoh, MMU.Nama_misi, MMU.Status FROM MENJALANKAN_MISI_UTAMA AS MMU, MISI_UTAMA AS MU WHERE MMU.Nama_misi = MU.Nama_misi""")

    print('ngetest 1')
    print(list_menjalankan_misiutama)
    print('ngetest 2')
    
    data = get_session_data(request)
    data['list_menjalankan_misiutama'] = list_menjalankan_misiutama

    return render(request, 'pemain_read_menjalankan_misiutama.html', data)