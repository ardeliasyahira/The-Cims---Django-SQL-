from django.shortcuts import render, HttpResponse, redirect
from utils.query import query
from home.views import get_session_data, is_authenticated, login
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def admin_read_misiutama(request):
    if not is_authenticated(request):
        return login(request)
    if request.session['role'] == 'pemain':
        return HttpResponse("Anda bukanlah admin")

    list_misiutama = query("SELECT * FROM MISI_UTAMA")
    list_misi_dijalanin = query("SELECT nama_misi FROM MENJALANKAN_MISI_UTAMA")

    list_list_misi_dijalanin = []

    for i in list_misi_dijalanin:
        list_list_misi_dijalanin.append(i['nama_misi'])

    for i in list_misiutama:
        i['ada'] = False

    for i in list_misiutama:
        if i['nama_misi'] in list_list_misi_dijalanin:
            i['ada'] = True

    print(list_misiutama)

    data = get_session_data(request)
    data['list_misiutama'] = list_misiutama


    return render(request, 'admin_read_misiutama.html', data)

def pemain_read_misiutama(request):
    if not is_authenticated(request):
        return login(request)
    if request.session['role'] == 'admin':
        return HttpResponse("Anda bukanlah pemain")

    list_misiutama = query("SELECT * FROM MISI_UTAMA")

    data = get_session_data(request)
    data['list_misiutama'] = list_misiutama

    return render(request, 'pemain_read_misiutama.html', data)

def pemain_detail_misiutama(request, nama):
    if not is_authenticated(request):
        return login(request)
    if request.session['role'] == 'admin':
        return HttpResponse("Anda bukanlah pemain")

    list_detailmisi = query(f"SELECT * FROM MISI WHERE nama = '{nama}'")
    print(list_detailmisi)


    data = get_session_data(request)
    data['list_detailmisi'] = list_detailmisi

    return render(request, 'detail_read_misiutama.html', data)

def admin_detail_misiutama(request, nama):
    if not is_authenticated(request):
        return login(request)
    if request.session['role'] == 'pemain':
        return HttpResponse("Anda bukanlah admin")

    list_detailmisi = query(f"SELECT * FROM MISI WHERE nama = '{nama}'")
    print(list_detailmisi)

    data = get_session_data(request)
    data['list_detailmisi'] = list_detailmisi

    return render(request, 'detail_read_misiutama.html', data)

@csrf_exempt
def admin_create_misiutama(request):
    if not is_authenticated(request):
        return login(request)
    if request.session['role'] == 'pemain':
        return HttpResponse("Anda bukanlah admin")

    if request.method == "POST":
        data = request.POST
        nama_misi = data.get('namaMisi')
        efek_energi = data.get('efekEnergi')
        efek_hubungan = data.get('efekHubungan')
        efek_kelaparan = data.get('efekKelaparan')
        syarat_energi = data.get('syaratEnergi')
        syarat_hubungan = data.get('syaratHubungan')
        syarat_kelaparan = data.get('syaratKelaparan')
        completion_time = data.get('completionTime')
        reward_koin = data.get('rewardKoin')
        reward_xp = data.get('rewardXP')
        desc = data.get('deskripsi')

        print(nama_misi)
        print(efek_energi)
        print(efek_hubungan)
        print(efek_kelaparan)
        print(syarat_energi)
        print(syarat_hubungan)
        print(syarat_kelaparan)
        print(completion_time)
        print(reward_koin)
        print(reward_xp)
        print(desc)

        query(f"""
        INSERT INTO MISI VALUES('{nama_misi}',{efek_energi},{efek_hubungan},{efek_kelaparan},
        {syarat_energi}, {syarat_hubungan}, {syarat_kelaparan},
        '{completion_time}', {reward_koin}, {reward_xp}, '{desc}')
        """)

        query(f"INSERT INTO MISI_UTAMA VALUES('{nama_misi}')")

        return redirect("/misi_utama/admin_read_misiutama/")

    return render(request, 'admin_create_misiutama.html')

# def admin_delete_misiutama(request):
#     if not is_authenticated(request):
#         return login(request)
#     if request.session['role'] == 'pemain':
#         return HttpResponse("Anda bukanlah admin")
    
#     query(f"DELETE FROM MISI_UTAMA WHERE ")