from datetime import datetime, timedelta

from rest_framework import status
from rest_framework.response import Response

from airControlBackend.pagination import StandardResultsSetPagination
from products.serializers import CitySerializer, CountrySerializer, CreateCitySerializer, MeasurementSerializer, \
    UserCitiesSerializer, CreateMeasurementSerializer, MessageSerializer
from products.models import City, Country, UserCities, Measurement, Message
from rest_framework import viewsets
from fcm_django.fcm import fcm_send_topic_message


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all().order_by('name')
    serializer_class = CountrySerializer


class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    permission_classes = ()

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateCitySerializer
        return super(CityViewSet, self).get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        some = serializer.create(serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)

    def get_queryset(self):
        username = self.request.user.id
        print(username)
        queryset = City.objects.all().order_by('name')
        gindex = self.request.query_params.get('index', None)
        if gindex == 'good':
            queryset = queryset.filter(index__range=(0, 50))
        if gindex == 'mid':
            queryset = queryset.filter(index__range=(50, 100))
        if gindex == 'bad':
            queryset = queryset.filter(index__range=(100, 300))
        return queryset


class MeasurementViewSet(viewsets.ModelViewSet):
    serializer_class = MeasurementSerializer
    permission_classes = ()
    queryset = Measurement.objects.all()

    def get_serializer_class(self):
        if self.action=='create':
            return CreateMeasurementSerializer
        return super(MeasurementViewSet, self).get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer = serializer.create(serializer.validated_data)
        print(serializer)
        return Response(status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        fcm_send_topic_message(topic_name=self.request.query_params['city'], message_body='Hello',
                               message_title='There is new data about ' + self.request.query_params['city'])

    def get_queryset(self):
        city_id = self.request.query_params.get('city_id', None)
        queryset = Measurement.objects.filter(city=city_id).order_by('-date')
        period = self.request.query_params.get('period', None)
        if period == 'day':
            queryset = queryset.filter(date__gte=datetime.now() - timedelta(days=1))
        if period == 'week':
            queryset = queryset.filter(date__gte=datetime.now() - timedelta(days=7))
        if period == 'month':
            queryset = queryset.filter(date__gte=datetime.now() - timedelta(days=30))
        return queryset


class UserCitiesViewSet(viewsets.ModelViewSet):
    serializer_class = UserCitiesSerializer
    queryset = UserCities.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.id)

    def get_queryset(self):
        user = self.request.user.id
        queryset = UserCities.objects.filter(user=user).order_by('city')
        return queryset


class MessagesViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all().order_by('-date')
    # pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(date=str(datetime.now()))
        fcm_send_topic_message(topic_name='chat', message_body='Hey! There is a new message in the chat for you',
                               message_title='New message!', data_message={"type": "chat", "user":self.request.user.id})


