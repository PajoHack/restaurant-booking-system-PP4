from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    opening_time = models.TimeField() # Opening time for the restaurant
    closing_time = models.TimeField() # Closing time for the restaurant

    def __str__(self):
        return self.name


class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    table_number = models.IntegerField()

    def __str__(self):
        return f"Table {self.table_number} at {self.restaurant.name}"


class Booking(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Confirmed'),
        ('X', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')

    def __str__(self):
        return f"Booking at {self.restaurant.name} for {self.guests} guests"


class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
