from rest_framework import serializers
from .models import Hotel, Reservation, Guest


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['guest_name', 'gender']


class ReservationSerializer(serializers.ModelSerializer):
    guests = GuestSerializer(many=True)

    class Meta:
        model = Reservation
        fields = ['id', 'hotel', 'checkin', 'checkout', 'guests']

    def create(self, validated_data):
        guests_data = validated_data.pop('guests')
        reservation = Reservation.objects.create(**validated_data)

        for guest in guests_data:
            Guest.objects.create(reservation=reservation, **guest)

        return reservation


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name']