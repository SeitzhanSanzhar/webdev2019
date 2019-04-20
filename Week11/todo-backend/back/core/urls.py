from django.conf.urls import url

from . import views

urlpatterns = [
    url('',views.index,name='index'),
    url('task_lists/', views.task_lists),
    url('task_lists/<int:id>', views.task_list_by_id),
    url('task_lists/<int:id>/tasks', views.get_tasks_by_id),
]