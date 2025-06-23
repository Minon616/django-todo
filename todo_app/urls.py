from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),                      # Show all tasks + add new
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),  # Mark complete
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),        # Delete task
]
