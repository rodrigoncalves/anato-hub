from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from authentication.ldap_auth import ldap_authentication
from auth_exceptions import LDAPConnectionError, LDAPCredentialError

# Login errors
SUCCESS = 0
INACTIVE_USER = 1
INVALID_LOGIN = 2
LDAP_CONNECTION_ERROR = 3

def authenticate_user(request, username, password):
    try:
        if ldap_authentication(username, password):
            if exist_user(username, password):
                login_user = authentication(username=username, password=password)
                login(request, login_user)
                return SUCCESS
            else:
                create_user(username, password)
                return INACTIVE_USER
    except LDAPCredentialError:
        return INVALID_LOGIN
    except LDAPConnectionError:
        return LDAP_CONNECTION_ERROR

def exist_user(username, password):
    try:
        user = User.objects.get(username=username, password=password, is_active=True)
        return True
    except:
        return False

def create_user(username, password):
    user = User.objects.create_user(username=username, email=None, password=password, is_active=False)
    return user
