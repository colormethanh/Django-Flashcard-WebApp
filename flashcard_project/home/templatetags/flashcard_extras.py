from django import template 
from django.utils.html import format_html
from django.utils.html import escape
from django.utils.safestring import mark_safe
from humanize import naturaltime
from django.utils import timezone


register = template.Library()

@register.filter
def set_details(set):
    owner = set.owner
    created_at = naturaltime(timezone.now() - set.created_at) 
    name = set.name 

    return format_html('{} <br>By {} | Created at: {}', name, owner, created_at)

@register.filter
def prnt_cards(cards):

    title = "<h3> Cards list </h3>"
    header = "<ul>"

    if cards :
        cardlst = [escape(c.front) for c in cards]
        cardlst = "".join([f"<li> {c} </li>" for c in cardlst ])
    else:
        cardlst = '<li> Currently there are no cards </li>'
    footer = "</ul>"

    
    return mark_safe(title + header + cardlst + footer)