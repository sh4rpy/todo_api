from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer, TaskHistorySerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [permissions.IsAuthenticated, ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'deadline', ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.request.user.task_set.all()

    @action(detail=True, methods=['GET'])
    def change_history(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskHistorySerializer(task.change_history, many=True)
        return Response(serializer.data)
