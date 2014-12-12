# -*- coding: utf-8 -*-

from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    if group in user.groups.all():
        user_has_group = True
    else:
        user_has_group = False

    return user_has_group