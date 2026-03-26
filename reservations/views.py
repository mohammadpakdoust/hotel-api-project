from rest_framework import generics
from django.db import models
from .models import Hotel, Reservation
from .serializers import HotelSerializer, ReservationSerializer

class HotelListView(generics.ListAPIView):
    serializer_class = HotelSerializer
    
    def get_queryset(self):
        queryset = Hotel.objects.all()
        checkin = self.request.query_params.get('checkin')
        checkout = self.request.query_params.get('checkout')
        
        if checkin and checkout:
            from django.db.models import Count, Q
            # Find hotels that are blocked (already at capacity) during the requested dates
            # An overlapping reservation is one where (res_checkin < checkout) AND (res_checkout > checkin)
            blocked_hotels = Hotel.objects.filter(
                reservations__checkin__lt=checkout,
                reservations__checkout__gt=checkin
            ).annotate(
                res_count=Count('reservations')
            ).filter(
                res_count__gte=models.F('capacity')
            ).values_list('id', flat=True)
            
            queryset = queryset.exclude(id__in=blocked_hotels)
            
        return queryset

class ReservationCreateView(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    # Optional: Customize the response if strictly required, 
    # but the User specifically asked for confirmation_number in the response earlier.
    # The default return will include confirmation_number because it's in the serializer fields.
