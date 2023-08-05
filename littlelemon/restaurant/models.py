# Assuming you have imported necessary modules and classes from Django
from django.db import models

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveIntegerField()
    bookingdate = models.DateTimeField()

    def __str__(self):
        return f"Booking for {self.name} on {self.bookingdate}"
