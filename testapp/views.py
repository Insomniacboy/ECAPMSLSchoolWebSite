import django
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def testfunction(request):
    return HttpResponse('yea it works')