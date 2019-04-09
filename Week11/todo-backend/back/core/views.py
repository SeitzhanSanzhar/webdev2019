# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from core.models import TaskList, Task


def index(request) :
    res = HttpResponse("Hello world")
    return res

def task_lists(request):
    all = TaskList.objects.all()
    json_all = [x.to_json() for x in all]
    return JsonResponse(json_all, safe=False)

def task_list_by_id(request, id):
    try:
        res = TaskList.objects.filter(id=id)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'de': str(e)}, safe=False)
    res_json = [x.to_json() for x in res]
    return JsonResponse(res_json, safe=False)

def get_tasks_by_id(request, id):
    try:
        res = TaskList.objects.filter(id=id)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'de': str(e)}, safe=False)
    res_json = [x.to_json() for x in res]
    return JsonResponse(res_json, safe=False)