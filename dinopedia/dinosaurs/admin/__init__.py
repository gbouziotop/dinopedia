# coding=utf-8
"""Dinosaurs app admin."""
from django.contrib import admin

from dinosaurs.admin.models import DinosaurAdmin
from dinosaurs.models import Dinosaur

admin.site.register(Dinosaur, DinosaurAdmin)
