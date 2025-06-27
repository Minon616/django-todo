from rest_framework import serializers
from .models import Task, TaskDetails

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskDetails
        fields = '__all__'
