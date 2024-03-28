# coding=utf-8
"""Dinosaur app admin models."""
from django.contrib import admin

from dinosaurs.admin.inlines import PhotoInline


class DinosaurAdmin(admin.ModelAdmin):
    list_filter = (
        'name',
        'eating_classification',
        'period_lived',
        'average_size'
    )
    list_per_page = 20
    search_fields = (
        'name',
        'eating_classification',
        'period_lived',
        'average_size'
    )
    inlines = (PhotoInline,)
    list_display = [
        'name', 'eating_classification', 'period_lived', 'average_size', 'typical_color'
    ]
    ordering = ('name',)
