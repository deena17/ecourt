from django import template
from django.conf import settings

register = template.Library()


@register.filter
def load_document(value):
    return settings.WEB_DIR+'chnccc'+value+'.pdf'

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter
def subtract(value, arg):
    return value - float(arg)

@register.filter
def replace_qtn(value):
    return value.replace("QTN","IN")

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists() 