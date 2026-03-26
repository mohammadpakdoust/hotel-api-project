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
    guests_list = GuestSerializer(many=True)
    hotel_name = serializers.CharField(write_only=True)

    class Meta:
        model = Reservation
        fields = ['hotel_name', 'checkin', 'checkout', 'guests_list', 'confirmation_number']
        read_only_fields = ['confirmation_number']

    def create(self, validated_data):
        guests_data = validated_data.pop('guests_list', [])
        hotel_name = validated_data.pop('hotel_name')
        
        # Get hotel
        hotel = Hotel.objects.filter(name=hotel_name).first()
        if not hotel:
            raise serializers.ValidationError({"hotel_name": f"Hotel '{hotel_name}' not found."})
        
        # Create reservation
        reservation = Reservation.objects.create(
            hotel=hotel,
            checkin=validated_data.get('checkin'),
            checkout=validated_data.get('checkout')
        )
        
        # Create guests attached to this reservation
        for guest_data in guests_data:
            Guest.objects.create(reservation=reservation, **guest_data)
            
        return reservation

    def to_representation(self, instance):
        # Strictly return ONLY confirmation_number in the response
        return {
            "confirmation_number": str(instance.confirmation_number)
        }
