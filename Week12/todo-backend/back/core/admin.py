# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from django.contrib import admin

from core.models import Task,TaskList

admin.site.register(Task)
admin.site.register(TaskList)