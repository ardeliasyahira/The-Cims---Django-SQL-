from django.shortcuts import render, HttpResponse
from utils.query import query
from home.views import get_session_data, is_authenticated, login

# Create your views here.
def admin_read_tokoh(request):
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] == 'pemain':
        return HttpResponse("Anda bukanlah admin")
    
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

    username = request.session['username']
    list_tokoh_pemain = query(f"SELECT * FROM tokoh WHERE username_pengguna = '{username}'")

    data = get_session_data(request)
    data['list_tokoh'] = list_tokoh_pemain

    print(data)

    return render(request, 'pemain_read_tokoh.html', data)