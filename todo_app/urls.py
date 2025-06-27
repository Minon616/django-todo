# todo_app/urls.py

from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/tasks', views.TaskViewSet, basename='task')
router.register(r'api/task-details', views.TaskDetailsViewSet, basename='taskdetails')

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('', include(router.urls)),  # Mount API routes
]
