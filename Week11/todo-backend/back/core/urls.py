from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('task_lists/', views.task_lists),
    path('task_lists/<int:id>', views.task_list_by_id),
    path('task_lists/<int:id>/tasks', views.get_tasks_by_id),
]