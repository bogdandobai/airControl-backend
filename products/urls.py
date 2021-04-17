from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from django.urls import include
from .views import CityViewSet, CountryViewSet, MeasurementViewSet, UserCitiesViewSet, MessagesViewSet

quickstart_router = DefaultRouter(trailing_slash=False)
quickstart_router.register('countries', CountryViewSet, basename='countries')
quickstart_router.register('cities', CityViewSet, basename='cities')
quickstart_router.register('measurements', MeasurementViewSet, basename='measurements')
quickstart_router.register('user-cities', UserCitiesViewSet, basename='user-cities')
quickstart_router.register('chat', MessagesViewSet, basename='chat')

urlpatterns = [
   url(r"^", include(quickstart_router.urls))
]
