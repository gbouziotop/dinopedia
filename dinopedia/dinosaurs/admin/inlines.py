# coding=utf-8
"""Dinosaur app admin inlines."""
from django.contrib import admin

from dinosaurs.admin.forms import PhotoInlineAdminForm
from dinosaurs.models import Photo


class PhotoInline(admin.StackedInline):
    readonly_fields = ('created',)
    model = Photo
    extra = 2
    max_num = 2
    inline_classes = ('grp-collapse grp-open',)
    form = PhotoInlineAdminForm
