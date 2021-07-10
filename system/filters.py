from django.db.models import fields
from django.db.models.base import Model
import django_filters
from .models import *

class RoomFilter(django_filters.FilterSet):
    class Meta:
        modal = Room
        fields = '__all__'