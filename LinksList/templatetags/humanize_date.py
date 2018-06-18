import arrow
from django import template

register = template.Library()


@register.filter
def humanize(value):
    return arrow.get(value).humanize()
