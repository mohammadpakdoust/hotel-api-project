from rest_framework import generics
from .models import Hotel, Reservation
from .serializers import HotelSerializer, ReservationSerializer

class HotelListView(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class ReservationCreateView(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except Exception as e:
            # This will show up in gunicorn logs and return a JSON error
            from rest_framework.response import Response
            import traceback
            error_msg = f"VIEW ERROR: {str(e)}\n{traceback.format_exc()}"
            print(error_msg)
            return Response({"detail": error_msg}, status=500)

    # Optional: Customize the response if strictly required, 
    # but the User specifically asked for confirmation_number in the response earlier.
    # The default return will include confirmation_number because it's in the serializer fields.
