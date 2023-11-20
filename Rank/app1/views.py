from django.shortcuts import render
from rest_framework import generics
from .serializers import *


# Create your views here.

class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class RankList(generics.ListAPIView):
    queryset = Rank.objects.all()
    serializer_class = RankSerializer
    
class RankDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rank.objects.all()
    serializer_class = RankSerializer