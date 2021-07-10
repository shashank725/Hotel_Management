import datetime
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
# Create your models here.
# from django.db.models.constraints import CheckConstraint

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Cat(models.Model):
    category = models.CharField(primary_key=True, max_length=100)
    description = models.TextField()
    category_picture = models.ImageField(upload_to = 'cat', null=True, blank=True)
    actual_price_range = models.CharField(max_length=100)
    offer_price_range = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.category}'

class Room(models.Model):
    room_category = models.ForeignKey(Cat, on_delete=models.CASCADE)
    number = models.IntegerField(unique=True)
    people = models.IntegerField()
    picture = models.ImageField(upload_to = 'room/', null=True, blank=True)
    actual_price = models.IntegerField()
    offer_price = models.IntegerField()

    def __str__(self):
        # return '%d : %s with People : %d' % (self.number, self.room_category, self.people)
        return 'Room with People - %d' %self.people
    
    # def clean(self, *args, **kwargs):
    #     if self.actual_price <= self.offer_price:
    #         raise ValidationError('offer price should be lower than the actual price')
    #     return super().clean(*args, **kwargs)
    
    def clean(self, *args, **kwargs):
        if self.offer_price <= 0:
            raise ValidationError('Price should be greater than Zero')
        elif self.actual_price <= self.offer_price:
            raise ValidationError('offer price should be lower than the actual price')
        return super().clean(*args, **kwargs)


# def clean_image(self):
#         IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
#         uploaded_image = self.cleaned_data.get("image",  False)
#         extension = str(uploaded_image).split('.')[-1]
#         file_type = extension.lower()
#         if not uploaded_image:       
#             raise ValidationError("please upload an Image") # handle empty image

#         if file_type not in IMAGE_FILE_TYPES:
#             raise ValidationError("File is not image.")
#         return uploaded_image

#     def clean(self):
#         cleaned_data = super().clean()
#         first_name = cleaned_data.get('first_name')
#         last_name  = cleaned_data.get('last_name')
#         if first_name == last_name:
#             raise ValidationError( "First name and last name cannot be the same." )



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
        # return f'{self.room} from {self.check_in} to {self.check_out}.'
        return f'{self.room}'
    
    def can_be_booked(self):
        now=timezone.now()
        if now + datetime.timedelta(days=1)<=self.check_in:
            return self.room


    # def get_room_category(self):
    #     room_categories=dict(self.room.category)
    #     room_category=room_categories.get(self.room.category)
    #     return room_category
    
    def get_cancel_booking_url(self):
        return reverse('system:CancelBookingView', args=[self.pk])

    def get_absolute_url(self):
        return reverse('system:BookingList',)
