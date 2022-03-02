from django.shortcuts import render
from .models import Events,Partner,Gallery
from rest_framework import viewsets
from .serializers import EventsSerializer, PartnerSerializer, GallerySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.http import HttpResponse

# Create your views here.



class EventsViewSets(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permisssion_classes = [IsAuthenticated]
    serializer_class = EventsSerializer
    queryset  = Events.objects.all()

class PartnerViewSets(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permisssion_classes = [IsAuthenticated]
    serializer_class = PartnerSerializer
    queryset  = Partner.objects.all()

class GalleryViewSets(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permisssion_classes = [IsAuthenticated]
    serializer_class = GallerySerializer
    queryset  = Gallery.objects.all()


def index(request):
    return render(request, 'be_the_leader/index.html')

def about(request):
    return render(request, 'be_the_leader/about.html')

def what_we_do(request):
    return render(request, 'be_the_leader/what_we_do.html')

def gallery(request):
    return render(request, 'be_the_leader/gallery.html')

def contact(request):
    return render(request, 'be_the_leader/contact.html')
