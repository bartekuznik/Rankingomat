from django.shortcuts import render
from rest_framework import generics, permissions, status

from . import serializers
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
        serializer = CustomUserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            custom_user = serializer.save()
            response_data = {
                'status': 1, 
                'username': custom_user.username,
                'money': custom_user.number_of_coins,
                'vip': int(custom_user.is_vip)
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response({'status': 0}, status=status.HTTP_400_BAD_REQUEST)

class CustomUserLogin(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = CustomUserLoginSerializer(data=request.data)
        if serializer.is_valid():
            custom_user_data = serializer.validate_custom_user(request.data)
            custom_user = authenticate(email=request.data['email'], password=request.data['password'])
            if custom_user:
                login(request, custom_user)
                return Response(custom_user_data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CustomUserLogout(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = ()
	def post(self, request):
		logout(request)
		return Response(status=status.HTTP_200_OK)

class UpdateVipStatusView(APIView):
    def post(self, request, format=None):
        serializer = ShopRequestSerializer(data=request.data)
        if serializer.is_valid():
            response_data = serializer.update_vip_status(serializer.validated_data)
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PurchaseTokensView(APIView):
    def post(self, request, format=None):
        serializer = TokenPurchaseRequestSerializer(data=request.data)
        if serializer.is_valid():
            try:
                response_data = serializer.add_tokens(serializer.validated_data)
                return Response(response_data, status=status.HTTP_200_OK)
            except serializers.ValidationError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateTokenView(APIView):
    def post(self, request, format=None):
        serializer = UpdateTokensRequestSerializer(data=request.data)
        if serializer.is_valid():
            try:
                response_data = serializer.update_tokens(serializer.validated_data)
                return Response(response_data, status=status.HTTP_200_OK)
            except serializers.ValidationError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)