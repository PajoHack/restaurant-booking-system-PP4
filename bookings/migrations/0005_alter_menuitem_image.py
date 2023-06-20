# Generated by Django 3.2.19 on 2023-06-20 17:22

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_menuitem_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dpwp5cavi/image/upload/v1687277051/menu_pic_q2kjau.jpg', max_length=255, verbose_name='image'),
        ),
    ]