from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse

def emrooz(request):
    now=timezone.now()
    return HttpResponse(str(now))
# Create your views here.
