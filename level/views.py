from django.shortcuts import redirect, render, HttpResponse
from utils.query import query
from database.views import get_session_data, is_authenticated, login
from django.views.decorators.csrf import csrf_exempt

def admin_read_level(request):
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] == 'pemain':
        return HttpResponse("Anda bukanlah admin")
    
    list_level = query("""SELECT *,
    CASE WHEN level NOT IN (SELECT level FROM TOKOH) THEN 'true' ELSE 'false'
    END AS can_delete
    FROM LEVEL
    ORDER BY level ASC;
    """)

    data = get_session_data(request)
    data['list_level'] = list_level
    if request.method == 'POST':
        if request.POST.get("DeleteButton") != None:
            request.session['Level'] = request.POST.get('DeleteButton')
            return delete_level(request)

    return render(request, 'admin_read_level.html', data)

def pemain_read_level(request):
    if not is_authenticated(request):
        return login(request)

    if request.session['role'] == 'admin':
        return HttpResponse("Anda bukanlah pemain")
    
    list_level = query("SELECT * FROM level")

    data = get_session_data(request)
    data['list_level'] = list_level


    return render(request, 'pemain_read_level.html', data)

@csrf_exempt
def create_level(request):
    if not is_authenticated(request):
        return login(request)
    
    if str(request.session['role']) == 'pemain':
        return HttpResponse("You are not authorized")
    
    if request.method != 'POST':
        return create_level_view(request)
    
    body = request.POST
    level = str(body.get('level_input'))
    xp = str(body.get('xp_input'))

    result = query(
        f"""
        INSERT INTO level VALUES
        ( '{level}', '{xp}')
    """
    )

    if not type(result) == int:
        return HttpResponse("Gagal Memasukkan Data")
    
    return admin_read_level(request)


def create_level_view(request):
    data = {}
    
    level = query(
        "SELECT * FROM level"
    )

    data['level'] = level

    return render(request, 'create_level.html', data)

def update_level_view(request, level, xp):
    if not is_authenticated(request):
        return login(request)
    
    if str(request.session['role']) == 'pemain':
        return HttpResponse("You are not authorized")
    data = get_session_data(request)

    data['level'] = level
    data['xp'] = xp

    if request.method == 'POST':
        return update_level(request)


    return render(request, 'update_level.html', data)

@csrf_exempt
def update_level(request):
    if not is_authenticated(request):
        return login(request)
    
    if str(request.session['role']) == 'pemain':
        return HttpResponse("You are not authorized")
    

    
    body = request.POST
    level = str(body.get('level_input'))
    xp = str(body.get('xp_input'))

    result = query(
        f"""
        UPDATE LEVEL
        SET xp = {xp}
        WHERE level = {level}
    """
    )

    return redirect('/level/admin/list_level')



def delete_level(request):
    if not is_authenticated(request):
        return login(request)
    
    if request.session['role'] == 'pemain':
        return HttpResponse("Anda bukanlah admin")
    
    level = request.session.get("Level")
    delete_query = query(f"""
        DELETE FROM LEVEL
        WHERE level = '{level}'
    """)

    return redirect('/level/admin/list_level')