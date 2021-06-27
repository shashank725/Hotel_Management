from django.contrib import admin
from .models import Room, Booking, Cat

# Register your models here.

admin.site.register(Cat)
admin.site.register(Room)
admin.site.register(Booking)