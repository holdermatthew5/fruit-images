from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BraeburnApple
from rest_framework import generics
from .serializer import AppleSerializer
from .models import BraeburnApple

class BraeburnAppleListView(generics.ListAPIView):
    queryset = BraeburnApple.objects.all()
    serializer_class = AppleSerializer

class BraeburnAppleDetailView(generics.RetrieveAPIView):
    queryset = BraeburnApple.objects.all()
    serializer_class = AppleSerializer

class BraeburnAppleCreateView(generics.CreateAPIView):
    queryset = BraeburnApple.objects.all()
    serializer_class = AppleSerializer

class BraeburnAppleUpdateView(generics.UpdateAPIView):
    queryset = BraeburnApple.objects.all()
    serializer_class = AppleSerializer

class BraeburnAppleDeleteView(generics.DestroyAPIView):
    queryset = BraeburnApple.objects.all()
    serializer_class = AppleSerializer
