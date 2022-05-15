from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from utils.query import query

# Create your views here.
def index(request):
    return render(request, 'index.html')

def is_authenticated(request):
    try:
        request.session['username']
        return True
    except:
        return False


def get_session_data(request):
    if not is_authenticated(request):
        return {}
    try:
        return {"username": request.session["username"], "role": request.session["role"]}
    except:
        return {}


def get_role(username, password):
    admin_query = query(
        f"SELECT username FROM ADMIN WHERE username = '{username}' AND password = '{password}'"
    )
    if type(admin_query) == dict:
        return "admin"

    player_query = query(
        f"SELECT username FROM pemain WHERE username = '{username}' AND password = '{password}'"
    )
    if type(player_query) == dict:
        return "pemain"

    return ""


@csrf_exempt
def login(request):
    next = request.GET.get("next")

    if request.method != "POST":
        return login_view(request)

    if is_authenticated(request):
        username = str(request.session["username"])
        password = str(request.session["password"])
    else:
        username = str(request.POST["username"])
        password = str(request.POST["password"])

    role = get_role(username, password)

    if role == "":
        return login_view(request)
    else:
        request.session["username"] = username
        request.session["password"] = password
        request.session["role"] = role
        request.session.set_expiry(0)
        request.session.modified = True

        if next != None and next != "None":
            return redirect(next)
        else:
            if role == "admin":
                return redirect("/home/admin_homepage")
            else:
                return redirect("/home/pemain_homepage")


def login_view(request):
    if is_authenticated(request):
        if str(request.session["role"]) == "admin":
            return redirect("/home/admin_homepage")
        else:
            return redirect("/home/pemain_homepage")

    return render(request, "login.html")


def logout(request):
    next = request.GET.get("next")

    if not is_authenticated(request):
        return redirect("/login")

    request.session.flush()
    request.session.clear_expired()

    if next != None and next != "None":
        return redirect(next)
    else:
        return redirect("/login")

def register_view(request):
    return render(request, "register.html")

@csrf_exempt
def register(request):
    if is_authenticated(request):
        if str(request.session["role"]) == "admin":
            return redirect("/home/admin_homepage")
        else:
            return redirect("/home/pemain_homepage")

    if request.method != "POST":
        return register_view(request)

    role1 = str(request.POST["role1"])
    
    if role1 == "admin":
        return register_admin(request)
    else:
        return register_pemain(request)

@csrf_exempt
def register_admin(request):
    next = request.GET.get("next")
    body = request.POST

    username = body.get("adminUsernameInput")
    password = body.get("adminPasswordInput")

    cari_akun_query = query(
        f"SELECT username FROM AKUN WHERE username = '{username}'"
    )

    if type(cari_akun_query) == list: 
        if len(cari_akun_query) == 0:
            akun_query = query(
                f"""
                INSERT INTO akun VALUES
                ('{username}')
            """
            )

    result = query(
        f"""
        INSERT INTO admin VALUES
        ('{username}', '{password}')
    """
    )

    if not type(result) == int:
        return HttpResponse("Anda gagal registrasi!")

    request.session["username"] = username
    request.session["password"] = password
    request.session["role"] = "admin"
    request.session.set_expiry(0)
    request.session.modified = True

    if next != None and next != "None":
        return redirect(next)
    else:
        return redirect("/home/admin_homepage")


@csrf_exempt
def register_pemain(request):
    next = request.GET.get("next")
    body = request.POST

    username = body["pemainUsernameInput"]
    email = body["pemainEmailInput"]
    password = body["pemainPasswordInput"]
    no_hp = body["pemainNoHpInput"]

    cari_akun_query = query(
        f"SELECT username FROM AKUN WHERE username = '{username}'"
    )

    # Kalau ada pemain yang sudah menjadi admin
    if type(cari_akun_query) == list: 
        if len(cari_akun_query) == 0:
            akun_query = query(
                f"""
                INSERT INTO akun VALUES
                ('{username}')
            """
            )

    result = query(
        f"""
        INSERT INTO pemain VALUES
        ('{username}', '{email}', '{password}', '{no_hp}')"""
    )
    
    print("PEMAIN:", result)
    
    request.session["username"] = username
    request.session["role"] = "pemain"
    request.session.set_expiry(0)
    request.session.modified = True

    if next != None and next != "None":
        return redirect(next)
    else:
        print("Pemain")
        return redirect("/home/pemain_homepage")

