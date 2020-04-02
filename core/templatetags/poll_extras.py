from django import template
register = template.Library()


@register.simple_tag
def to_list(*args):
    return args
