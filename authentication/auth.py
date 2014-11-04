# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from authentication.ldap_auth import ldap_authentication
from auth_exceptions import LDAPUserDoesNotExist, LDAPConnectionError, \
    LDAPCredentialError


# Login errors
SUCCESS = 0
INACTIVE_USER = 1
INVALID_LOGIN = 2
LDAP_CONNECTION_ERROR = 3


def authenticate_user(request, username, password):
    try:
        user = exist_user(username, password)
        if ldap_authentication(username, password):
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return SUCCESS
                elif user.last_login == user.date_joined:
                    return INACTIVE_USER
                else:
                    return INVALID_LOGIN
            else:
                create_user(username, password)
                return INACTIVE_USER
        elif user is not None:
            inactivate_user(user)

        return INVALID_LOGIN

    except LDAPUserDoesNotExist:
        if user is not None:
            inactivate_user(user)
        return INVALID_LOGIN
    except LDAPCredentialError:
        if user is not None:
            inactivate_user(user)
        return INVALID_LOGIN
    except LDAPConnectionError:
        return LDAP_CONNECTION_ERROR


def exist_user(username, password):
    login_user = authenticate(username=username, password=password)
    return login_user


def create_user(username, password):
    user = User.objects.create_user(username=username, email=None, password=password)
    user.is_active = False
    user.save()
    return user


def inactivate_user(user):
    user.is_active = False
    user.save()
    return user


def authenticate_user_without_ldap(request, username, password):
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return SUCCESS
        else:
            return INACTIVE_USER
    else:
        return INVALID_LOGIN
