from django.shortcuts import render
from rest_framework import generics, permissions, status
from .serializers import *
from django.contrib.auth import login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication


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

class CustomUserRegistration(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        serializer = CustomUserRegisterSerializer(data = request.data)
        if serializer.is_valid():
            custom_user = serializer.create(request.data)
            if custom_user:
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)

class CustomUserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    def post(self, request):
        serializer = CustomUserLoginSerializer(data = request.data)
        if serializer.is_valid():
            custom_user = serializer.validate_custom_user(request.data)
            login(request, custom_user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status = status.HTTP_400_BAD_REQUEST)

class CustomUserLogout(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = ()
	def post(self, request):
		logout(request)
		return Response(status=status.HTTP_200_OK)