import datetime

from rest_framework import serializers

from . import custom_fields
from .models import Task, TaskHistory


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    status = custom_fields.CustomChoiceField(choices=Task.STATUS_CHOICES)

    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'description', 'creation_time', 'status', 'deadline', )

    def validate(self, data):
        if data.get('deadline') and data['deadline'] < datetime.date.today():
            raise serializers.ValidationError('Дата завершения меньше сегодняшней')
        return data


class TaskHistorySerializer(serializers.ModelSerializer):
    task = serializers.ReadOnlyField(source='task.title')

    class Meta:
        model = TaskHistory
        fields = ('id', 'task', 'title', 'description', 'creation_time', 'status', 'deadline', )
