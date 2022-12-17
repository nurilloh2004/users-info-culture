# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from parler import admin as parler_admin
from adminsortable2 import admin as adminsortable2_admin

from . import models


class PollItemInline(adminsortable2_admin.SortableInlineAdminMixin, parler_admin.TranslatableTabularInline, admin.TabularInline):
    model = models.Item
    extra = 1
    min_num = 2
    max_num = 4


@admin.register(models.Poll)
class PollAdmin(parler_admin.TranslatableAdmin):
    list_display = ('question', 'date', 'vote_count', 'is_published')
    inlines = [PollItemInline, ]


@admin.register(models.Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('poll', 'ip', 'created_at')
    list_filter = ('poll', 'created_at')
