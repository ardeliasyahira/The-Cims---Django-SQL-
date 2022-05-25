from django.shortcuts import render, HttpResponse
from utils.query import query
from home.views import get_session_data, is_authenticated, login
from .models import Tokoh
from .forms import TokohForm

# Create your views here.
def admin_read_tokoh(request):
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] == 'pemain':
        return HttpResponse("Anda bukanlah admin")
    
    if request.POST.get('NamaTokoh') != None:
        return admin_detail_tokoh(request)

    list_tokoh = query("SELECT * FROM tokoh")

    data = get_session_data(request)
    data['list_tokoh'] = list_tokoh

    print(data)

    return render(request, 'admin_read_tokoh.html', data)

def pemain_read_tokoh(request):
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] == 'admin':
        return HttpResponse('Anda bukanlah pemain')

    if request.POST.get("NamaTokoh") != None:
        return pemain_detail_tokoh(request)

    username = request.session['username']
    list_tokoh_pemain = query(f"SELECT * FROM tokoh WHERE username_pengguna = '{username}'")

    data = get_session_data(request)
    data['list_tokoh'] = list_tokoh_pemain

    print(data)

    return render(request, 'pemain_read_tokoh.html', data)

def create_tokoh(request):
    form = TokohForm()
    if request.method == 'POST':
        form = DonasiForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tokoh/pemain_read_tokoh')
    response = {'form': form}
    return render(request, 'create_tokoh.html', response)
    
def admin_detail_tokoh(request):
    if is_authenticated(request):
        print("terotentikasi")

        nama_tokoh = request.POST.get('NamaTokoh')
        data_query = query(f"SELECT * FROM TOKOH WHERE Nama LIKE '%{nama_tokoh}%'")
        data = get_session_data(request)
        data["list"] = data_query
        print(data_query)

        return render(request, "detail_tokoh.html", data)
    else:
        print("tidak terotentikasi")
        return login(request)

def pemain_detail_tokoh(request):
    if is_authenticated(request):
        print("terotentikasi")

        nama_tokoh = request.POST.get('NamaTokoh')
        username = request.session.get("username")
        data_query = query(f"SELECT * FROM TOKOH WHERE  Username_pengguna ='{username}' AND Nama LIKE '%{nama_tokoh}%'")
        data = get_session_data(request)
        data["list"] = data_query
        print(data_query)
        return render(request, "detail_tokoh.html", data)
    else:
        print("tidak terotentikasi")
        return login(request)

def pemain_update_tokoh(request) :
    if is_authenticated(request):
        print("terotentikasi")

        nama_tokoh = request.POST.get('NamaTokoh')
        username = request.session.get("username")
        data_query = query(f"SELECT * FROM TOKOH WHERE  Username_pengguna ='{username}' AND Nama LIKE '%{nama_tokoh}%'")
        data = get_session_data(request)
        data["list"] = data_query
        print(data_query)
        return render(request, "pemain_update_tokoh.html", data)
    else:
        print("tidak terotentikasi")
        return login(request)
