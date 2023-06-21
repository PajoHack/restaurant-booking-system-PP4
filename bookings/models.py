from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    our_story = models.TextField(blank=True)
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
    CATEGORY_CHOICES = [
        ('ST', 'Starters'),
        ('PI', 'Pizza'),
        ('PA', 'Pasta'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default='ST')
    image = CloudinaryField('image', default='https://res.cloudinary.com/dpwp5cavi/image/upload/v1687277051/menu_pic_q2kjau.jpg')

    def __str__(self):
        return self.name


class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()