from django import template 
from django.utils.html import format_html
from humanize import naturaltime
from django.utils import timezone


register = template.Library()

@register.filter
def set_details(set):
    owner = set.owner
    created_at = naturaltime(timezone.now() - set.created_at) 
    name = set.name 

    return format_html('{} <br>By {} | Created at: {}', name, owner, created_at)
