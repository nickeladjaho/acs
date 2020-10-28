from django import template


register = template.Library()

@register.filter
def print_file_content(f):
        return f.read()