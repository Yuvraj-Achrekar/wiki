from django import template
import random
from .. import util

register = template.Library()

@register.simple_tag
def random_generator():
    entries = util.list_entries()
    if entries:
        random_entry = random.choice(entries)
        return random_entry
    else:
        return '' 