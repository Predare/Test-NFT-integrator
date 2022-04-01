from rest_framework import serializers
from .models import Token

class TokenSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    unique_hash = serializers.CharField(max_length=20) # уникальный хэш
    tx_hash = serializers.CharField(max_length=100) # хэш транзакции создания токена
    media_url = serializers.URLField() # урл с произвольным изображением
    owner = serializers.CharField(max_length=100) # адрес пользователя в сети Ethereum

    def create(self, validated_data):
        """
        Create and return a new `Token` instance, given the validated data.
        """
        return Token.objects.create(**validated_data)