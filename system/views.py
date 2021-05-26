from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone


# Create your views here.

def homepage(request):
    return render(request, 'system/index.html')

def sights(request):
    return render(request, 'system/sights.html')
