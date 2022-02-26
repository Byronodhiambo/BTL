from posixpath import basename
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('events', views.EventsViewSets, basename='events')
router.register('partner', views.PartnerViewSets, basename='partner')
router.register('gallery', views.GalleryViewSets, basename='events')


app_name = 'be_the_leader'

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls)),

]