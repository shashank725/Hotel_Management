from django.db import models

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
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in=models.DateTimeField()
    check_out=models.DateTimeField()

    def __str__(self):
        return f'{self.room} from {self.check_in} to {self.check_out}'
