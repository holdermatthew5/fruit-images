from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BraeburnApple
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from .serializer import AppleSerializer
from .models import BraeburnApple

class BraeburnAppleListView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = BraeburnApple.objects.all()
    serializer_class = AppleSerializer

class BraeburnAppleDetailView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = BraeburnApple.objects.all()
    serializer_class = AppleSerializer

class BraeburnAppleCreateView(generics.CreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = BraeburnApple.objects.all()
    serializer_class = AppleSerializer

class BraeburnAppleUpdateView(generics.UpdateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = BraeburnApple.objects.all()
    serializer_class = AppleSerializer

class BraeburnAppleDeleteView(generics.DestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = BraeburnApple.objects.all()
    serializer_class = AppleSerializer
