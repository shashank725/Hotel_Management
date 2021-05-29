from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.

class Room(models.Model):
    number=models.IntegerField()
    categories={
        ('STD','Standard'), ('CR', 'Connecting Room'), ('DEL', 'Deluxe'), ('KIN', 'King'), ('QUE', 'Queen'), ('SUI', 'Suite'), ('PEN', 'Penthouse')
    }
    category=models.CharField(max_length=3, choices=categories, default='STD')
    beds=models.IntegerField(default=1)

    def __str__(self):
        return '%d : %s with %d beds.' % (self.number, self.category, self.beds)

class Booking(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in=models.DateTimeField()
    check_out=models.DateTimeField()

    def __str__(self):
        return f'{self.room} from {self.check_in} to {self.check_out}.'

    def get_room_category(self):
        room_categories=dict(self.room.categories)
        room_category=room_categories.get(self.room.category)
        return room_category

    def get_cancel_booking_url(self):
        return reverse('system:CancelBookingView', args=[self.pk])

    def get_absolute_url(self):
        return reverse('system:BookingList',)