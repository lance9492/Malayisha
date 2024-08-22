from django.db import models
from django.contrib.auth.models import User
from store.models import Order

class Country(models.Model):
    name = models.CharField(max_length=100)
    is_sadc = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.country.name}"

class Courier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=100)
    countries_served = models.ManyToManyField(Country)

    def __str__(self):
        return self.user.username

class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=50, default='Pending')
    delivery_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    delivery_city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    delivery_address = models.TextField()

    def __str__(self):
        return f"Delivery for Order {self.order.id} to {self.delivery_city}, {self.delivery_country}"