
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_1(value):
    if value > actual_price:
        raise ValidationError(
            _('%(value)s is greater than Actual Price'),
            params={'value': value},
        )



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
    global actual_price
    actual_price = models.IntegerField()
    offer_price = models.IntegerField(validators=[validate_even])

    def __str__(self):
        return '%d : %s with People : %d' % (self.number, self.room_category, self.people)
