# -*- coding: utf-8 -*-


def create_specific_exam(name_class):
    app_name = name_class.lower()

    module = __import__(app_name + '.models', fromlist=[name_class])
    class_ = getattr(module, name_class)
    instance = class_()

    return instance
