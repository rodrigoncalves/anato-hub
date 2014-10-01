from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.context_processors import csrf

# Login errors
INACTIVE_USER = 1
INVALID_LOGIN = 2

def sign_in(request):
    if request.user.is_authenticated():
        return render_to_response('home_search.html',
            context_instance=RequestContext(request)
        )

    if request.method == 'GET':
        return render_to_response('sign_in.html',
            context_instance=RequestContext(request)
        )

    username = request.POST.get('username')
    password = request.POST.get('password')

    login_user = authenticate(username=username, password=password)
    login_error = None

    csrf_token = {}
    csrf_token.update(csrf(request))

    if login_user is not None:
        if login_user.last_login != login_user.date_joined:
            if login_user.is_active:
                login(request, login_user)
                return redirect('/', csrf_token)
            else:
                login_error = INACTIVE_USER
        else:
            login(request, login_user)
            return redirect('/', csrf_token)
    else:
        login_error = INVALID_LOGIN

    return render_to_response(
        'sign_in.html',
        {'login_error': login_error, 'modal_error': True},
        context_instance=RequestContext(request)
    )

@login_required(login_url='/login/')
def log_out(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def first_access(request):

    # salva no banco

    return render_to_response(
        'home.html', {
        'first_access': True, },
        context_instance=RequestContext(request)
    )


@login_required(login_url='/login/')
def home(request):
    return render_to_response(
        'home.html'
    )
