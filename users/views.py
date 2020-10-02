from rest_framework import viewsets, permissions, mixins

from .serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny, ]
