from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, TaskDetails

# DRF Imports
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer, TaskDetailsSerializer

# -------------------------------
# Template-Based Views (READ ONLY)
# -------------------------------

def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    details = {d.task_id: d for d in TaskDetails.objects.all()}
    return render(request, 'todo_app/task_list.html', {
        'tasks': tasks,
        'details': details
    })

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('/')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('/')

# -------------------------------
# API Views (Protected with JWT)
# -------------------------------

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  # Require JWT token

class TaskDetailsViewSet(viewsets.ModelViewSet):
    queryset = TaskDetails.objects.all()
    serializer_class = TaskDetailsSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]  # Require JWT token

    def perform_create(self, serializer):
        serializer.save()
