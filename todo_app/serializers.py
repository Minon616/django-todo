from rest_framework import serializers
from todo_app.models import Task, TaskDetails

class TaskDetailsSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(read_only=True)

    class Meta:
        model = TaskDetails
        fields = ['description', 'image']

class TaskSerializer(serializers.ModelSerializer):
    details = TaskDetailsSerializer(source='taskdetails', read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'completed', 'created_at', 'details']
