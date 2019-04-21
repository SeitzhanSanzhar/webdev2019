import json

from core import models
from core.serializers import TaskListSerializer, TaskSerializer

from django.views import View
from django.http import JsonResponse


class TasksById(View):

    def post(self, request, id):
        data = json.loads(request.body)
        data['task_list'] = id
        ser = TaskSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201)
        return JsonResponse(ser.errors, status=400)

    def get(self, request, id):
        try:
            tasks = models.Task.objects.get(task_list=id)
        except models.Task.DoesNotExist as e:
            return JsonResponse({'error': 'tasklist with such id does not exist'}, safe=False)

            ser = TaskSerializer(tasks, many=True)

        return JsonResponse(ser.data, status=201, safe=False)

class TaskList(View):

    def delete(self, request, id):
        try:
            task_list = models.TaskList.objects.get(id=id)
        except models.TaskList.DoesNotExist as e:
            return JsonResponse({'error': 'tasklist with such id does not exist'}, safe=False, status=404)

        task_list.delete()
        ser = TaskListSerializer(task_list)
        return JsonResponse(ser.data)

    def get(self, request, id):
        try:
            task_list = models.TaskList.objects.get(id=id)
        except models.TaskList.DoesNotExist as e:
            return JsonResponse({'dee': 'tasklist with such id does not exist'}, safe=False, status=404)
            ser = TaskListSerializer(task_list)
        return JsonResponse(ser.data, safe=False)

class TaskLists(View):

    def get(self, request):
        task_lists = models.TaskList.objects.all()
        ser = TaskListSerializer(task_lists, many=True)
        return JsonResponse(ser.data, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        ser = TaskListSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201)
        return JsonResponse(ser.errors)

