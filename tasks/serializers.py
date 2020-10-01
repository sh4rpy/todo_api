import datetime

from rest_framework import serializers

from . import custom_fields
from .models import User, Task, TaskHistory


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    status = custom_fields.CustomChoiceField(choices=Task.STATUS_CHOICES)

    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'description', 'creation_time', 'status', 'deadline', )

    def validate(self, data):
        if data['deadline'] < datetime.date.today():
            raise serializers.ValidationError('Дата завершения меньше сегодняшней')
        return data


class TaskHistorySerializer(serializers.ModelSerializer):
    task = serializers.ReadOnlyField(source='task.title')

    class Meta:
        model = TaskHistory
        fields = ('id', 'task', 'title', 'description', 'creation_time', 'status', 'deadline', )
