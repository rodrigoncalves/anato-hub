# -*- coding: utf-8 -*-


class LDAPConnectionError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class LDAPCredentialError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
