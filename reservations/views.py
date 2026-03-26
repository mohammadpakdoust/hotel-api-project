from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Hotel, Reservation
from .serializers import HotelSerializer, ReservationSerializer


class HotelListView(APIView):
    def get(self, request):
        checkin = request.GET.get('checkin')
        checkout = request.GET.get('checkout')

        hotels = Hotel.objects.all()

        # Optional filtering (basic)
        if checkin and checkout:
            hotels = hotels.exclude(
                reservations__checkin__lt=checkout,
                reservations__checkout__gt=checkin
            )

        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)


class ReservationCreateView(APIView):
    def post(self, request):
        serializer = ReservationSerializer(data=request.data)

        if serializer.is_valid():
            reservation = serializer.save()
            return Response(
                {"confirmation_number": str(reservation.id)},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)