from django import template
from django.http import HttpResponseRedirect
from django.urls import reverse
import random
from .. import util

register = template.Library()

@register.simple_tag
def random_generator():
    random_entry = random.choice(util.list_entries())
    return random_entry
