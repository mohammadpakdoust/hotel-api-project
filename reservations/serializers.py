from rest_framework import serializers
from .models import Hotel, Guest, Reservation

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['guest_name', 'gender']

class ReservationSerializer(serializers.ModelSerializer):
    guests_list = GuestSerializer(many=True, source='guests')
    hotel_name = serializers.CharField(write_only=True)

    class Meta:
        model = Reservation
        fields = ['hotel_name', 'checkin', 'checkout', 'guests_list', 'confirmation_number']
        read_only_fields = ['confirmation_number']

    def create(self, validated_data):
        guests_data = validated_data.pop('guests') # From source='guests'
        hotel_name = validated_data.pop('hotel_name')
        
        # Get hotel by name as per requirement
        hotel = Hotel.objects.get(name=hotel_name)
        
        reservation = Reservation.objects.create(hotel=hotel, **validated_data)
        
        for guest_data in guests_data:
            guest = Guest.objects.create(**guest_data)
            reservation.guests.add(guest)
            
        return reservation
