# Generated by Django 3.2.19 on 2023-06-21 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0006_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='table',
        ),
        migrations.AddField(
            model_name='booking',
            name='table',
            field=models.ManyToManyField(to='bookings.Table'),
        ),
    ]
