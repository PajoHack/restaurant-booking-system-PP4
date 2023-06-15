from django.contrib import admin
from .models import Restaurant, Table, Booking, MenuItem

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Table)
admin.site.register(Booking)
admin.site.register(MenuItem)
