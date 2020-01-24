from django.shortcuts import render
from rest_framework import generics
from .serializers import EventListSerializer, EventDetailSerializer
from .models import *

class EventCreateView(generics.CreateAPIView):
    serializer_class = EventDetailSerializer

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventDetailSerializer
    queryset = Event.objects.all()

class EventListView(generics.ListAPIView):
    serializer_class = EventListSerializer
    queryset = Event.objects.all()
