from django.contrib import admin
from .models import Restaurant, Table, Booking, MenuItem

# Register your models here.
# admin.site.register(Restaurant)
# admin.site.register(Table)
admin.site.register(Booking)
# admin.site.register(MenuItem)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'description', 'price', 'category')
    list_filter = ('category',)
    search_fields = ['name']
    
    
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    
    list_display = ('table_number', 'seats')
    list_filter = ('table_number', 'seats')
    
    
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'address', 'opening_time', 'closing_time')
    list_filter = ('name', 'address')
    
    
