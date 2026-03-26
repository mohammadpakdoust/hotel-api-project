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
        print(f"Creating reservation for hotel: {validated_data.get('hotel_name')}")
        try:
            guests_data = validated_data.pop('guests')
            hotel_name = validated_data.pop('hotel_name')
            
            # Get hotel by name as per requirement
            try:
                hotel = Hotel.objects.get(name=hotel_name)
            except Hotel.DoesNotExist:
                print(f"Hotel not found: {hotel_name}")
                raise serializers.ValidationError({"hotel_name": f"Hotel with name '{hotel_name}' does not exist."})
            
            # Create reservation
            reservation = Reservation.objects.create(hotel=hotel, **validated_data)
            print(f"Reservation instance created: {reservation.id}")
            
            # Create and link guests
            for guest_data in guests_data:
                guest = Guest.objects.create(**guest_data)
                reservation.guests.add(guest)
            
            print(f"Successfully created reservation {reservation.confirmation_number}")
            return reservation
        except Exception as e:
            print(f"ERROR creating reservation: {str(e)}")
            raise e
