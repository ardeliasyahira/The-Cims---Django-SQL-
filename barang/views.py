import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render, HttpResponse
from utils.query import query
from home.views import get_session_data, is_authenticated, login
from django.views.decorators.csrf import csrf_exempt
from .forms import PemainCreateMenggunakanBarang

def admin_read_barang(request):
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] == 'pemain':
        return HttpResponse("Anda bukanlah admin")
    
    list_menggunakan_barang = query("""
    SELECT * 
    FROM MENGGUNAKAN_BARANG MB, KOLEKSI_JUAL_BELI KJ
    WHERE MB.id_barang = KJ.id_koleksi
    """)

    data = get_session_data(request)
    data['list_menggunakan_barang'] = list_menggunakan_barang

    return render(request, 'admin_read_barang.html', data)

def pemain_read_barang(request):
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] == 'admin':
        return HttpResponse("Anda bukanlah pemain")
    
    list_menggunakan_barang = query("""
    SELECT * 
    FROM MENGGUNAKAN_BARANG MB, KOLEKSI_JUAL_BELI KJ
    WHERE MB.id_barang = KJ.id_koleksi
    """)

    data = get_session_data(request)
    data['list_menggunakan_barang'] = list_menggunakan_barang

    return render(request, 'pemain_read_barang.html', data)

@csrf_exempt
def pemain_menggunakan_barang(request):
    response = {}
    form = PemainCreateMenggunakanBarang(request.POST or None)
    response['form'] = form
    username_aktif = request.session['username']

    list_tokoh_masuk = query(f""" SELECT T.nama from TOKOH T WHERE T.username_pengguna = '{username_aktif}' """)
    print("list tokoh masuk")
    print(list_tokoh_masuk)
    print("list tokoh yg di index")
    print(list_tokoh_masuk[0]['nama'])
    
    form.fields['nama_tokoh'].initial = [(list_tokoh_masuk[0]['nama'], list_tokoh_masuk[0]['nama'])]
    form.fields['nama_tokoh'].choices = [(list_tokoh_masuk[i]['nama'], list_tokoh_masuk[i]['nama']) for i in range(len(list_tokoh_masuk))]

    if 'nama_tokoh' in request.GET: 
        nama_tokoh = request.GET['nama_tokoh']
    else:
        nama_tokoh = list_tokoh_masuk[0]['nama']

    semua_barang = query(f""" SELECT DISTINCT KT.id_koleksi 
                                FROM KOLEKSI_TOKOH KT , BARANG B 
                                    WHERE KT.id_koleksi = B.id_koleksi """)

    barang_milik_tokoh = query(f""" SELECT DISTINCT KT.id_koleksi 
                                        FROM KOLEKSI_TOKOH KT, BARANG B 
                                            WHERE KT.id_koleksi = B.id_koleksi AND KT.nama_tokoh = '{nama_tokoh}'""")
    
    form.fields['barang'].choices = [(semua_barang[i]['id_koleksi'], semua_barang[i]['id_koleksi']) for i in range(len(semua_barang))]

    if 'nama_tokoh' in request.GET:
        list_barang_milik_tokoh = [barang_milik_tokoh[i]['id_koleksi'] for i in range(len(barang_milik_tokoh))]
        print("barang punya tokoh")
        print(list_barang_milik_tokoh)
        dd_barangtokoh = {'barang_milik_tokoh' : list_barang_milik_tokoh}
        return JsonResponse(data=dd_barangtokoh, safe=False)

    if request.method == 'POST' and form.is_valid(): 
        nama_tokoh = form.cleaned_data['nama_tokoh']
        barang = form.cleaned_data['barang']

        # if nama_tokoh and barang: 
            # energi_tokoh = query(f""" SELECT T.energi from TOKOH T WHERE  T.nama = '{nama_tokoh}'""")
            # energi_bisadipakai = query(f""" SELECT B.tingkat_energi FROM BARANG B WHERE B.id_koleksi = '{barang}'; """)

            # if energi_tokoh[0]['energi'] >= energi_bisadipakai[0]['tingkat_energi'] :
        query(f""" INSERT INTO MENGGUNAKAN_BARANG MB VALUES('{username_aktif}', '{nama_tokoh}', '{datetime.datetime.now()}', '{barang}'""")
        print("udah insert")

        return HttpResponseRedirect('/barang/pemain_create_barang')
            # else:
                # response["message"] = "Energi tokoh tidak mencukupi sehingga barang tidak dapat digunakan!"
    
    else:
        #  request.method == 'POST' and not form.is_valid():
        response["message"] = "Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu!"

    return render(request, 'pemain_create_barang.html', response)



    








