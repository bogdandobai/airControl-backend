from django.db import models
# Create your models here.
from accounts.models import User


class Country(models.Model):
    name=models.TextField()

    class Meta:
      ordering = ['name']

    def __str__(self):
       return self.name


class City(models.Model):
    name = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    country = models.ForeignKey(
      Country,
      on_delete=models.CASCADE,
      verbose_name='countries',
      related_name='countries'
    )
    index = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self) :
        return self.name


class Measurement(models.Model):
    NO2 = models.IntegerField(blank=True, null=True)
    PM10 = models.IntegerField(blank=True, null=True)
    PM25 = models.IntegerField(blank=True, null=True)
    O3 = models.IntegerField(blank=True, null=True)
    SO2 = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name='cities',
        related_name='measure'
    )

    class Meta:
        ordering = ['date']


class UserCities(models.Model):
    user = models.IntegerField(blank=True, null=True, auto_created=True)
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name='cities',
    )
    notifications = models.BooleanField(blank=True, null=True, default=True)

    def __str__(self):
        return str(self.user) + " " + self.city.name


class Message(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='users',
        # auto_created=True,
        # blank=True,
        # null=True
    )
    message = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.message

