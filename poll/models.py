# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from parler import models as parler_models


class Poll(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        question=models.CharField(max_length=255, unique=True)
    )

    is_published = models.BooleanField(default=True)
    date = models.DateField(default=datetime.date.today)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Poll")
        verbose_name_plural = _("Polls")

    def __unicode__(self):
        return f"{ self.safe_translation_getter('question', self.id) }"

    def __str__(self):
        return f"{ self.safe_translation_getter('question', self.id) }"

    def get_vote_count(self):
        return Vote.objects.filter(poll=self).count()
    vote_count = property(fget=get_vote_count)

    def get_cookie_name(self):
        return 'poll_%s' % self.pk


class Item(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        value=models.CharField(max_length=255, unique=True)
    )

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    position = models.SmallIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['position']

    def __unicode__(self):
        return f"{ self.safe_translation_getter('value', self.id) }"

    def __str__(self):
        return f"{ self.safe_translation_getter('value', self.id) }"

    def get_vote_count(self):
        return Vote.objects.filter(item=self).count()
    vote_count = property(fget=get_vote_count)


class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, verbose_name='voted item', on_delete=models.CASCADE)
    ip = models.GenericIPAddressField(verbose_name='ip address')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Vote")
        verbose_name_plural = _("Votes")

    def __unicode__(self):
        return self.ip

    def __str__(self):
        return self.ip
