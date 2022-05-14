from django.shortcuts import render, HttpResponse
from utils.query import query
from home.views import get_session_data, is_authenticated, login
# Create your views here.

def admin_read_misiutama(request):
    if not is_authenticated(request):
        return login(request)
    if request.session['role'] == 'pemain':
        return HttpResponse("Anda bukanlah admin")

    list_misiutama = query("SELECT * FROM MISI_UTAMA")

    data = get_session_data(request)
    data['list_misiutama'] = list_misiutama

    return render(request, 'admin_read_misiutama.html', data)
