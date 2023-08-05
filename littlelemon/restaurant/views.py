from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer
from .models import Booking
from .serializers import BookingSerializer
from rest_framework import viewsets

def index(request):
    return render(request, 'index.html', {})

def sayHello(request):
    return HttpResponse('Hello World')

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer