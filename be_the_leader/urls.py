from posixpath import basename
from django.contrib import admin
from django.urls import path
from . import views



app_name = 'be_the_leader'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('what_we_do/', views.what_we_do, name='what_we_do'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('feedback/', views.feedback, name='feedback'),   



]
