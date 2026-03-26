from django.db import models
import uuid

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Guest(models.Model):
    guest_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.guest_name

class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reservations')
    guests = models.ManyToManyField(Guest, related_name='reservations')
    checkin = models.DateField()
    checkout = models.DateField()
    confirmation_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"Reservation {self.confirmation_number} at {self.hotel.name}"
