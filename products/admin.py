from django.contrib import admin

from products.models import City
from products.models import Country, Measurement, UserCities
# Register your models here.

admin.site.register(City)
admin.site.register(Country)
admin.site.register(Measurement)
admin.site.register(UserCities)
