from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Room(models.Model):
    number=models.IntegerField()
    categories={
        ('STD','Standard'), ('CR', 'Connecting Room'), ('DEL', 'Deluxe'), ('KIN', 'King'), ('QUE', 'Queen'), ('SUI', 'Suite'), ('PEN', 'Penthouse')
    }
    categories_amount = {
        ('STD', 100), ('CR', 200), ('DEL', 300), ('KIN', 400), ('QUE', 500), ('SUI', 600), ('PEN', 700)
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
    payment_status_choices = {
        ('SUC', 'SUCCESS'),
        ('FAI', 'FAILURE'),
        ('PEN', 'PENDING')}
    payment_status = models.CharField(max_length=3, choices=payment_status_choices, default='PEN')
    amount = models.FloatField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True, default=None)
    datetime_of_payment = models.DateTimeField(default=timezone.now)
    # After payment
    razorpay_order_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_payment_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_signature = models.CharField(max_length=500, null=True, blank=True)
    
    
    def save(self, *args, **kwargs):
        if self.order_id is None and self.datetime_of_payment and self.id:
            self.order_id = self.datetime_of_payment.strftime('GLUG%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)
        
    
    def __str__(self):
        return f'{self.room} from {self.check_in} to {self.check_out}.'

    def get_room_category(self):
        room_categories=dict(self.room.categories)
        room_category=room_categories.get(self.room.category)
        return room_category

    def get_payment_status(self):
        payment=dict(self.payment_status)
        status=payment.get(self.payment_status)
        return status

    def get_cancel_booking_url(self):
        return reverse('system:CancelBookingView', args=[self.pk])

    def get_absolute_url(self):
        return reverse('system:BookingList',)
