from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Cat(models.Model):
    category = models.CharField(primary_key=True, max_length=100)
    category_picture = models.ImageField(upload_to = 'cat', null=True, blank=True)
    actual_prize_range = models.CharField(max_length=100)
    offer_prize_range = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.category}'

class Room(models.Model):
    room_category = models.ForeignKey(Cat, on_delete=models.CASCADE)
    number = models.IntegerField()
    people = models.IntegerField()
    picture = models.ImageField(upload_to = 'room/', null=True, blank=True)
    actual_prize = models.CharField(max_length=100)
    offer_prize = models.CharField(max_length=100)

    def __str__(self):
        return '%d : %s with People : %d' % (self.number, self.room_category, self.people)

class Booking(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in=models.DateTimeField()
    check_out=models.DateTimeField()
    payment_status_choices = {
        ('SUCCESS', 'SUCCESS'),
        ('FAILURE', 'FAILURE'),
        ('PENDING', 'PENDING')}
    payment_status = models.CharField(max_length=10, choices=payment_status_choices, default='PENDING')
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

    # def get_room_category(self):
    #     room_categories=dict(self.room.category)
    #     room_category=room_categories.get(self.room.category)
    #     return room_category
    
    def get_cancel_booking_url(self):
        return reverse('system:CancelBookingView', args=[self.pk])

    def get_absolute_url(self):
        return reverse('system:BookingList',)
