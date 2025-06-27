# todo_app/urls.py

from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TaskDetailsViewSet

# Set up API routes using DRF's router
router = DefaultRouter()
router.register(r'api/tasks', TaskViewSet, basename='task')
router.register(r'api/taskdetails', TaskDetailsViewSet, basename='taskdetails')

urlpatterns = [
    # Template-based views (used in browser)
    path('', views.task_list, name='task_list'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),

    # API routes
    path('', include(router.urls)),
]
