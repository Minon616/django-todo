# todo_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, TaskDetails

# REST Framework imports
from rest_framework import viewsets
from .serializers import TaskSerializer, TaskDetailsSerializer

# -------------------------------
# Template-Based Views (HTML Form)
# -------------------------------

def task_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        image = request.FILES.get('image')

        if title:
            task = Task.objects.create(title=title)
            TaskDetails.objects.create(
                task=task,
                description=description,
                image=image
            )
        return redirect('/')

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
# REST API Views (DRF ViewSets)
# -------------------------------

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer


class TaskDetailsViewSet(viewsets.ModelViewSet):
    queryset = TaskDetails.objects.all()
    serializer_class = TaskDetailsSerializer
