from django.contrib import admin
from .models import Task, TaskDetails  # import both models

admin.site.register(Task)
admin.site.register(TaskDetails)  # register TaskDetails too
