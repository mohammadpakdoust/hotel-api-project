from django.db import models
import uuid

class Hotel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reservations')
    checkin = models.DateField()
    checkout = models.DateField()

    def __str__(self):
        return f"{self.hotel.name} - {self.id}"


class Guest(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='guests')
    guest_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.guest_name