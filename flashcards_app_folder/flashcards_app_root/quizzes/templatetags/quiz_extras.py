from django import template

register = template.Library()

@register.filter
def split_choices(value, delimiter=','):
    return value.split(delimiter)
