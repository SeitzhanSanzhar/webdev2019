# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TaskList(models.Model):
    name = models.CharField(max_length=100)
    def to_json(self) :
        res = {'id':self.id,'name':self.name}
        return res
    def __str__(self):
        return "Name: " + self.name;

class Task(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    due_on = models.DateTimeField(blank=True,null=True)
    status = models.CharField(max_length=50)
    def to_json(self):
        res = {
            'id':self.id,
            'name':self.name,
            'created_at':self.created_at,
            'due_on':self.due_on,
            'status':self.status
        }
        return res
    def __str__(self):
        return "Name: " + self.name;
