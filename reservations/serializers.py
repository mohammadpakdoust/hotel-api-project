from rest_framework import serializers
from .models import Hotel, Reservation, Guest


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['guest_name', 'gender']


class ReservationSerializer(serializers.ModelSerializer):
    guests_list = GuestSerializer(many=True, source='guests')
    hotel_name = serializers.CharField(write_only=True)

    class Meta:
        model = Reservation
        fields = ['hotel_name', 'checkin', 'checkout', 'guests_list']

    def create(self, validated_data):
        guests_data = validated_data.pop('guests')
        hotel_name = validated_data.pop('hotel_name')

        hotel = Hotel.objects.get(name=hotel_name)
        reservation = Reservation.objects.create(hotel=hotel, **validated_data)

        for guest in guests_data:
            Guest.objects.create(reservation=reservation, **guest)

        return reservation


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name']