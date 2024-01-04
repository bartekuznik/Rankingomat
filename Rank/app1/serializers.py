from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import CustomUser, Rank
from django.contrib.auth import authenticate

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'email',
            'password',
            'number_of_coins',
            'is_vip'
        ]

class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = [
            'player',
            'win_number'
        ]

class CustomUserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        custom_user = CustomUser.objects.create_user(
            email = validated_data['email'],
            username = validated_data['username'],
             password = validated_data['password'])
        custom_user.save()
        return custom_user

class CustomUserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate_custom_user(self, validated_data):
        custom_user = authenticate(username=validated_data['email'], password=validated_data['password'])
        if not custom_user:
            raise ValidationError('Invalid login credentials')

        # Preparing the custom response data
        return {
            'username': custom_user.username,
            'money': custom_user.number_of_coins,
            'vip': int(custom_user.is_vip)  # Converting boolean to int (0 or 1)
        }

class ShopRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    vip = serializers.IntegerField()

    def update_vip_status(self, validated_data):
        try:
            user = CustomUser.objects.get(username=validated_data['username'])
            user.is_vip = validated_data['vip']
            user.save()
            return {
                'username': user.username,
                'vip': user.is_vip
            }
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("User not found.")


class TokenPurchaseRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    tokens = serializers.IntegerField()

    def add_tokens(self, validated_data):
        try:
            user = CustomUser.objects.get(username=validated_data['username'])
            user.number_of_coins += validated_data['tokens']
            user.save()
            return {
                'username': user.username,
                'money': user.number_of_coins
            }
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("User not found.")
