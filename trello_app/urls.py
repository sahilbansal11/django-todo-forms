from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('new_task', views.add_task, name='add_task'),
  path('new_task_form', views.add_task_form, name='add_task_form'),
  path('new_list', views.add_task_list, name='add_task_list'),
  path('new_list_form', views.add_task_list_form, name='add_task_list_form'),
  path(
    'task_details/<int:input_id>',
    views.task_details,
    name='task_detail_page'
  )
]