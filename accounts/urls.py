from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from django.urls import include
from accounts.views import UserViewSet

quickstart_router = DefaultRouter(trailing_slash=False)
quickstart_router.register('users', UserViewSet, basename='users')

urlpatterns = [
   url(r"^", include(quickstart_router.urls))
]
