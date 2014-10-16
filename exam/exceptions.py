# -*- coding: utf-8 -*-


class ModelDoesNotExist(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class InvalidParameter(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
