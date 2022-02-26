from dataclasses import fields
from rest_framework import serializers
from .models import Gallery, Partner, Events

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id', 'title', 'content', 'image', 'created_on']

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'title', 'content', 'image', 'addted_on']


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'title', 'content', 'image', 'added_on']