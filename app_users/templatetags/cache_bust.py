from django import template
from django.utils.timezone import now

register = template.Library()


@register.simple_tag
def cache_bust():
    # Append a timestamp to bust the cache
    return int(now().timestamp())
