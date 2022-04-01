from django.db import models

# Create your models here.
class Token(models.Model):
    unique_hash = models.CharField(max_length=20, unique=True) # уникальный хэш
    tx_hash = models.CharField(max_length=100) # хэш транзакции создания токена
    media_url = models.URLField() # урл с произвольным изображением
    owner = models.CharField(max_length=100) # адрес пользователя в сети Ethereum

    class Meta:
        ordering = ['id']