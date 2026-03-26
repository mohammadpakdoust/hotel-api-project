from django.contrib import admin
from .models import Hotel, Guest, Reservation

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'capacity')

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('guest_name', 'gender')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('confirmation_number', 'hotel', 'checkin', 'checkout')
