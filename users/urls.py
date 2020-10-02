from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken

from .views import UserViewSet


router = DefaultRouter()
router.register('register', UserViewSet, basename='register')
urlpatterns = [
    path('', include(router.urls)),
    path('token/', ObtainAuthToken.as_view(), name='token_obtain_pair'),
]
