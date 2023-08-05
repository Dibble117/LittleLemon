from rest_framework import serializers
from .models import Menu
from .models import Booking
from .models import MenuItem

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        extra_kwargs = {
            'bookingdate': {'format': '%Y-%m-%dT%H:%M:%SZ'}  # ISO 8601 format
        }

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory']