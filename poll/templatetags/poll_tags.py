# -*- coding: utf-8 -*-

from random import choice

from django import template
from django.template.loader import render_to_string

from poll import models


register = template.Library()


@register.simple_tag(takes_context=True)
def poll(context):
    request = context['request']

    try:
        poll = choice(models.Poll.objects.filter(translations__language_code=request.LANGUAGE_CODE, is_published=True))
    except:
        return ''

    poll_template = "poll/result.html" if poll.get_cookie_name() in request.COOKIES else "poll/poll.html"

    return render_to_string(poll_template, {
        'request': request,
        'poll': poll,
        'items': poll.item_set.filter(translations__language_code=request.LANGUAGE_CODE),
    })


@register.simple_tag
def percentage(poll, item):
    poll_vote_count = poll.get_vote_count()

    if poll_vote_count > 0:
        return float(item.get_vote_count()) / float(poll_vote_count) * 100
