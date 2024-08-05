from django.contrib import admin
from .models import Table, MenuItem, Booking

# Register your models here.

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'capacity')
    list_filter = ('capacity',)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')
    list_filter = ('price',)
    search_fields = ('name', 'description')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'table', 'date', 'time', 'guests')
    list_filter = ('date', 'time')
    search_fields = ('user__username', 'user__email')
