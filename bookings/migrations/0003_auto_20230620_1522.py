# Generated by Django 3.2.19 on 2023-06-20 15:22

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_restaurant_our_story'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='image',
            field=cloudinary.models.CloudinaryField(default='https://www.freepik.com/free-vector/food-menu-logo-set_715731.htm#query=placeholder%20restaurant&position=32&from_view=keyword&track=ais', max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]