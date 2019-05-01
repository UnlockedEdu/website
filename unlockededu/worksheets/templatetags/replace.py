import re

from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()


@register.filter
@stringfilter
def replace_spaces(string):
    print(string)
    return re.sub(" ", "&nbsp;", string)

