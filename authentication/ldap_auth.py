# -*- coding: utf-8 -*-

import ldap
from auth_exceptions import LDAPConnectionError, LDAPCredentialError, \
    LDAPUserDoesNotExist
from configs.ldap import LDAP_DOMAIN, LDAP_SERVER, DN, DN_SECRET, \
    LDAP_BASE


def ldap_authentication(username, password):
    try:
        connection = initialize_ldap_connection()
        if search_user(connection, username):
            username = username + LDAP_DOMAIN
            connection.simple_bind_s(username, password)
            return True
        else:
            raise LDAPUserDoesNotExist("User does not exist")
    except ldap.INVALID_CREDENTIALS:
        raise LDAPCredentialError("Invalid Credentials")
    except ldap.SERVER_DOWN:
        raise LDAPConnectionError("Can't contact LDAP server")

def initialize_ldap_connection():
    server = LDAP_SERVER

    connection = ldap.initialize(server)
    connection.protocol_version = ldap.VERSION3
    connection.set_option(ldap.OPT_REFERRALS, 0)
    connection.simple_bind_s(DN, DN_SECRET)

    return connection

def search_user(connection, username):
    scope = ldap.SCOPE_SUBTREE
    filter = "(&(sAMAccountName=" + username + "))"
    timeout = 60

    search = connection.search(LDAP_BASE, scope, filter)
    user_type, user = connection.result(search, timeout)

    if user[0][0] is not None:
        return True
    else:
        return False
