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
        print(validated_data)
        custom_user = authenticate(
            username=validated_data['email'],
            password=validated_data['password'])
        if not custom_user:
            raise ValidationError('No User')
        return custom_user
