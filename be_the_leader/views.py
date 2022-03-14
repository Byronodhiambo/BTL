from django.shortcuts import render
from .models import Events, Message,Partner,Gallery,WhatWeDo
from django.http import HttpResponseRedirect
import datetime
from .forms import MessageForm
from django.urls import reverse

# Create your views here.


def index(request):
    events = Events.objects.all()
    current_time = datetime.datetime.now()
    return render(request, 'be_the_leader/index.html',{'events':events, 'current_time':current_time})#

def about(request):
    return render(request, 'be_the_leader/about.html')

def what_we_do(request):
    return render(request, 'be_the_leader/what_we_do.html')

def gallery(request):
    return render(request, 'be_the_leader/gallery.html')

def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']

            data = Message(name=name, email=email, subject=subject, content=content)
            data.save()
            
            return HttpResponseRedirect(reverse('be_the_leader:feedback'))


    return render(request, 'be_the_leader/contact.html')



def feedback(request):
    return render(request, 'be_the_leader/thanks.html')
    
