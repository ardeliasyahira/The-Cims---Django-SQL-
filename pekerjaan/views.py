import datetime
from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse
from utils.query import query
from home.views import get_session_data, is_authenticated, login
from .forms import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def read_pekerjaan(request):
    if not is_authenticated(request):
        return login(request)
    
    list_pekerjaan = query("SELECT * FROM PEKERJAAN")

    data = get_session_data(request)
    data['list_pekerjaan'] = list_pekerjaan

    if request.session['role'] == "admin":
        if request.POST.get("NamaPekerjaanDelete") != None:
                request.session['Kerja'] = request.POST.get('NamaPekerjaanDelete')
                return admin_delete_pekerjaan(request)
        return render(request, 'admin_read_pekerjaan.html', data)
    else:
        return render(request, 'pemain_read_pekerjaan.html', data)

@csrf_exempt
def read_bekerja(request):
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] == "admin":
        list_bekerja = query("SELECT * FROM BEKERJA")
        data = get_session_data(request)
        data['list_bekerja'] = list_bekerja
        
        return render(request, "admin_read_bekerja.html", data)
        
    if request.session['role'] == "pemain":
        username = request.session['username']
        list_bekerja = query(f"SELECT * FROM BEKERJA WHERE username_pengguna = '{username}'")
        data = get_session_data(request)
        data['list_bekerja'] = list_bekerja
        
        return render(request, "pemain_read_bekerja.html", data)

@csrf_exempt
def admin_create_pekerjaan(request) :
    response = {}
    form = createPekerjaanForms(request.POST or None)
    response['form'] = form
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] != "admin":
        redirect ('/')

    if(request.method == 'POST'):
        nama_pekerjaan = request.POST['nama_pekerjaan']
        base_honor = request.POST['base_honor']
        print(nama_pekerjaan)
        print(base_honor)
        query(f"""INSERT INTO PEKERJAAN VALUES
                            ('{nama_pekerjaan}', {base_honor});""")
        return redirect('/pekerjaan/read_pekerjaan')
    return render(request, 'admin_create_pekerjaan.html')

@csrf_exempt
def admin_update_pekerjaan(request, nama_pekerjaan) :
    response = {}
    form = updatePekerjaanForms(request.POST or None)
    response['form'] = form

    if not is_authenticated(request):
        return login(request)

    if request.session['role'] != "admin":
        redirect ('/')

    nama_fix = query(f"""SELECT * FROM PEKERJAAN p WHERE '{nama_pekerjaan}' = p.nama;""")
    response['nama_fix'] = nama_fix
    print(response['nama_fix'])
    print(nama_fix)

    form.fields['nama_pekerjaan'].initial = nama_pekerjaan
    form.fields['base_honor'].initial = nama_fix['base_honor']

    if(request.method == 'POST'):
        base_honor = request.POST['base_honor']
        query(f"""UPDATE PEKERJAAN
                        SET base_honor = {base_honor}
                        WHERE nama = '{nama_pekerjaan}';""")
    return render(request, 'admin_update_pekerjaan.html')

@csrf_exempt
def admin_delete_pekerjaan(request):
    if not is_authenticated:
        return login(request)

    nama = request.session.get("Kerja")
    update_query = query(f"""
    DELETE FROM pekerjaan WHERE nama = '{nama}'
    """)

    return redirect("/pekerjaan/admin_read_pekerjaan")

def pemain_create_bekerja(request):
    response = {}
    username = request.session['username']
    print(username)
    try:
        print("masuk")
        data = query(f""" SELECT T.nama, T.pekerjaan, P.base_honor
                            FROM TOKOH T, PEKERJAAN P 
                                WHERE T.pekerjaan = P.nama AND T.username_pengguna = '{username}'""")
        response['data'] = data
        print(data)

        if request.method == 'POST':
            base_honor = query(f"""SELECT p.base_honor FROM PEKERJAAN p 
                                        WHERE p.nama = '{request.POST['pekerjaan']}'""")[0]['base_honor']
            level = query(f"""SELECT T.level FROM TOKOH T 
                                WHERE T.nama = '{request.POST['nama']}' AND T.username_pengguna = '{username}'""")[0]['level']
            print(base_honor)
            print(level)
            print(honor)
            honor = level * base_honor
            info_keberangkatan = query(f""" SELECT MAX(B.keberangkatan_ke)
                                                FROM BEKERJA B 
                                                    WHERE B.nama_tokoh = '{request.POST['nama']}' 
                                                        AND B.nama_pekerjaan = '{request.POST['pekerjaan']}' """)[0]['max_keberangkatan']
            
            print(info_keberangkatan)
            if info_keberangkatan is None: 
                info_keberangkatan = 0
            else: 
                info_keberangkatan += 1
            
            query(f""" INSERT INTO BEKERJA VALUES('{username}', '{request.POST['nama']}', '{datetime.datetime.now()}', 
                    '{request.POST['pekerjaan']}', '{info_keberangkatan}', '{honor}'""")
            
            return HttpResponseRedirect('/pekerjaan/read_bekerja')
    except Exception as e: 
        print(e)
        print("gamasuk")
        return HttpResponseRedirect('/')
    
    return render(request, 'pemain_create_bekerja.html', response)




