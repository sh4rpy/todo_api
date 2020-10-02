from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken

from .views import TaskViewSet


router = DefaultRouter()
router.register('', TaskViewSet, basename='tasks')
urlpatterns = [
    path('', include(router.urls)),
]
