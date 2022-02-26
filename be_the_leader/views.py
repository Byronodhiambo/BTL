from .models import Events,Partner,Gallery
from rest_framework import viewsets
from .serializers import EventsSerializer, PartnerSerializer, GallerySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

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
   