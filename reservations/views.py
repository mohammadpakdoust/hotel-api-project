from rest_framework import generics
from .models import Hotel, Reservation
from .serializers import HotelSerializer, ReservationSerializer

class HotelListCreateView(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class ReservationCreateView(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    # Optional: Customize the response if strictly required, 
    # but the User specifically asked for confirmation_number in the response earlier.
    # The default return will include confirmation_number because it's in the serializer fields.
