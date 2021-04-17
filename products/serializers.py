from rest_framework import serializers

from products.models import Country, Measurement, UserCities, Message, City
from accounts.serializers import UserSerializer


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'id', 'name'
        )


class CreateCitySerializer(serializers.Serializer):

    cities = serializers.ListField(
        child=serializers.DictField()
    )

    def update(self, instance, validated_data):
        raise NotImplemented

    def create(self, validated_data):
        cities = []
        for city in validated_data["cities"]:
            cities.append(City(**city))
        cities = City.objects.bulk_create(cities)
        return cities


class CitySerializer(serializers.ModelSerializer):
    # country = CountrySerializer()

    # def get_country(self, album):
    #     return ', '.join([str(country) for country in City.country])

    class Meta:
        model = City
        fields = ('id', 'name', 'country', 'url', 'latitude', 'longitude', 'index')

    def to_representation(self, instance):
        data = super(CitySerializer, self).to_representation(instance)
        data["country"] = CountrySerializer(instance.country).data
        return data


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ('id', 'NO2', 'PM10', 'PM25', 'O3', 'SO2', 'date', 'city')

    # def to_representation(self, instance):
    #     data = super(MeasurementSerializer, self).to_representation(instance)
    #     data["city"] = CitySerializer(instance.city).data
    #     return data
    #


class CreateMeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ('id', 'NO2', 'PM10', 'PM25', 'O3', 'SO2', 'date', 'city')

    # measures = serializers.ListField(
    #     child=serializers.DictField()
    # )
    #
    # def update(self, instance, validated_data):
    #     raise NotImplemented
    #
    # def create(self, validated_data):
    #     measures = []
    #     for measure in validated_data["measures"]:
    #         measures.append(Measurement(**measure))
    #     measures = Measurement.objects.bulk_create(validated_data["measures"])
    #     return measures


class UserCitiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCities
        fields = ('id', 'user', 'city', 'notifications')

    def to_representation(self, instance):
        data = super(UserCitiesSerializer, self).to_representation(instance)
        data["city"] = CitySerializer(instance.city).data
        return data


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('id', 'user', 'message', 'date')

    def to_representation(self, instance):
        data = super(MessageSerializer, self).to_representation(instance)
        data["user"] = UserSerializer(instance.user).data
        return data