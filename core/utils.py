# -*- coding: utf-8 -*-

def convert_date_format(date):
    split_date = date.split('/')
    date = split_date[2] + '-' + split_date[1] + '-' + split_date[0]
    return date
