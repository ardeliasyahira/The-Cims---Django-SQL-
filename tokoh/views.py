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

def pemain_update_tokoh(request) :
    if is_authenticated(request):
        print("terotentikasi")

        nama_tokoh = request.POST.get('Nama')
        username = request.session.get("Username")
        data_query = query(f"SELECT * FROM TOKOH WHERE  username_pengguna ='{username}' AND nama LIKE '%{nama_tokoh}%'")
        data = get_session_data(request)
        data["list"] = data_query
        print(data_query)
        return render(request, "pemain_update_tokoh.html", data)
    else:
        print("tidak terotentikasi")
        return login(request)
