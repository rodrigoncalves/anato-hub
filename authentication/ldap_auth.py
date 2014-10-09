# -*- coding: utf-8 -*-

import ldap
from auth_exceptions import LDAPConnectionError, LDAPCredentialError
from configs.ldap import LDAP_DOMAIN, LDAP_SERVER


def initialize_ldap_connection():
    server = LDAP_SERVER

    connection = ldap.initialize(server)
    connection.protocol_version = ldap.VERSION3
    connection.set_option(ldap.OPT_REFERRALS, 0)

    return connection


def ldap_autentication(username, password):
    connection = initialize_ldap_connection()
    username = username + LDAP_DOMAIN

    try:
        connection.simple_bind_s(username, password)

        return True
    except ldap.INVALID_CREDENTIALS:
        raise LDAPCredentialError("Invalid Credentials")
    except ldap.SERVER_DOWN:
        raise LDAPConnectionError("Can't contact LDAP server")
