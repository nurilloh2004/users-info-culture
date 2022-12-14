# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render


from . import models, utils


def vote(request, poll_id):
    if request.is_ajax():

        try:
            poll = models.Poll.objects.get(translations__language_code=request.LANGUAGE_CODE, pk=poll_id)
        except models.Poll.DoesNotExist:
            return HttpResponse('Wrong parameters', status=400)

        item_id = request.GET.get("item", False)

        if not item_id:
            return HttpResponse('Wrong parameters', status=400)

        try:
            item = models.Item.objects.get(translations__language_code=request.LANGUAGE_CODE, pk=item_id)
        except:
            return HttpResponse('Wrong parameters', status=400)

        models.Vote.objects.create(
            poll=poll,
            ip=request.META['REMOTE_ADDR'],
            item=item,
        )
        response = HttpResponse(status=200)
        utils.set_cookie(response, poll.get_cookie_name(), poll_id)

        return response
    return HttpResponse(status=400)


def poll_view(request, poll_id):
    try:
        poll = models.Poll.objects.get(translations__language_code=request.LANGUAGE_CODE, pk=poll_id)
    except:
        return HttpResponse('Wrong parameters', status=400)

    try:
        items = models.Item.objects.filter(translations__language_code=request.LANGUAGE_CODE, poll=poll)
    except:
        return HttpResponse('Wrong parameters', status=400)

    context = {'poll': poll, 'items': items}

    if poll.get_cookie_name() in request.COOKIES:
        return render(request, "poll/result.html", context)
    else:
        return render(request, "poll/poll.html", context)


def result(request, poll_id):
    try:
        poll = models.Poll.objects.get(translations__language_code=request.LANGUAGE_CODE, pk=poll_id)
    except:
        return HttpResponse('Wrong parameters', status=400)

    try:
        items = models.Item.objects.filter(translations__language_code=request.LANGUAGE_CODE, poll=poll)
    except:
        return HttpResponse('Wrong parameters', status=400)

    context = {'poll': poll, 'items': items, }

    return render(request, "poll/result.html", context)


def percentage(poll, item):
    poll_vote_count = poll.get_vote_count()
    if poll_vote_count > 0:
        return float(item.get_vote_count()) / float(poll_vote_count) * 100
