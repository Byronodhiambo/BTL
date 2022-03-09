from django.shortcuts import render
from .models import Events,Partner,Gallery,WhatWeDo
from django.http import HttpResponse
import datetime

# Create your views here.


def index(request):
    # events = Events.objects.all()
    # current_time = datetime.datetime.now()
    return render(request, 'be_the_leader/index.html')#{'events':events, 'current_time':current_time}

def about(request):
    return render(request, 'be_the_leader/about.html')

def what_we_do(request):
    return render(request, 'be_the_leader/what_we_do.html')

def gallery(request):
    return render(request, 'be_the_leader/gallery.html')

def contact(request):
    return render(request, 'be_the_leader/contact.html')
