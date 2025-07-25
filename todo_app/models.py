from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class TaskDetails(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='tasks/', blank=True, null=True)

    def __str__(self):
        return f"Details for: {self.task.title}"
