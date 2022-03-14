import email
from site import addsitedir
from unicodedata import name
from xml.parsers.expat import model
from django.db import models

# Create your models here.

class Events(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=600)    
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    time = models.DateTimeField()
    created_on = models.DateField(auto_created=True)

class Gallery(models.Model):
    category = models.CharField(max_length=100, default='social events')
    title  =models.CharField(max_length=100)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    added_on = models.DateTimeField(auto_created=True)

class Partner(models.Model):
    title  =models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    added_on = models.DateTimeField(auto_created=True)

class WhatWeDo(models.Model):
    category = models.CharField(max_length=100)
    content = models.TextField()
    added_on = models.DateTimeField(auto_created=True)

class Message(models.Model):
    name = models.CharField(max_length=100)
    email  = models.EmailField()
    subject =  models.CharField(max_length=100)
    content = models.TextField()
    date_added = models.DateTimeField(auto_created=True, null=True )