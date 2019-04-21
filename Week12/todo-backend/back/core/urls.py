from django.urls import path

from . import views

urlpatterns = [
    path('task_lists/', views.TaskLists.as_view()),
    path('task_lists/<int:id>', views.TaskList.as_view()),
    path('task_lists/<int:id>/tasks', views.TasksById.as_view()),
]