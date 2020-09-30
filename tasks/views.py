from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, mixins
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import UserSerializer, TaskSerializer


class UserViewSet(mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny, ]


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [permissions.IsAuthenticated, ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'deadline']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.request.user.user_tasks.all()
