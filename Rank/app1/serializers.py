from rest_framework import serializers
from .models import CustomUser, Rank

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