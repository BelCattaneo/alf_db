from django import template
from django.template import Template

register = template.Library()

@register.simple_tag()
def active(request, pattern):
    import re
    if re.search(pattern, request.path):
        return "active"
    else:
        return ""