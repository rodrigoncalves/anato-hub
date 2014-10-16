# -*- coding: utf-8 -*-

from exam.exceptions import ModelDoesNotExist, InvalidParameter


def create_specific_exam(name_class):
    try:
        app_name = name_class.lower()

        module = __import__(app_name + '.models', fromlist=[name_class])
        class_ = getattr(module, name_class)
        instance = class_()

        return instance
    except ImportError:
            raise ModelDoesNotExist('Model does not exist')
    except ValueError:
            raise InvalidParameter('Invalid parameter')
