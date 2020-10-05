import datetime

from rest_framework import serializers

from . import custom_fields
from .models import Task, TaskHistory


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    status = custom_fields.CustomChoiceField(choices=Task.STATUS_CHOICES)

    class Meta:
        model = Task
        fields = '__all__'

    def validate(self, data):
        if data.get('deadline') and data['deadline'] < datetime.date.today():
            raise serializers.ValidationError('Дата завершения меньше сегодняшней')
        return data


class TaskHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskHistory
        fields = '__all__'
