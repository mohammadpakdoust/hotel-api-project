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
        try:
            guests_data = validated_data.pop('guests')
            hotel_name = validated_data.pop('hotel_name')
            
            # Step 1: Hotel Lookup
            hotel = Hotel.objects.filter(name=hotel_name).first()
            if not hotel:
                raise serializers.ValidationError({"hotel_name": f"Hotel '{hotel_name}' not found."})
            
            # Step 2: Reservation Creation
            reservation = Reservation.objects.create(
                hotel=hotel,
                checkin=validated_data.get('checkin'),
                checkout=validated_data.get('checkout')
            )
            
            # Step 3: Guest Creation and Linking
            for guest_data in guests_data:
                guest = Guest.objects.create(**guest_data)
                reservation.guests.add(guest)
            
            return reservation
        except Exception as e:
            import traceback
            # Force the error into a field called 'debug_error' which will be visible in the script output
            error_details = {
                "error": str(e),
                "traceback": traceback.format_exc(),
                "hotel_name": hotel_name if 'hotel_name' in locals() else "unknown",
                "validated_data": str(validated_data)
            }
            raise serializers.ValidationError(error_details)
