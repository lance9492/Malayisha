from django.contrib import admin
from .models import Courier, Delivery, Country, City

admin.site.register(Courier)
admin.site.register(Delivery)
admin.site.register(Country)
admin.site.register(City)