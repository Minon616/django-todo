from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, TaskDetails

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


# Mark a task as completed
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('/')

# Delete a task
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('/')