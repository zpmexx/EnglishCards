from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """User model"""
    phone_number = models.IntegerField(verbose_name="Numer telefonu", blank=True, null=True)
    
    def __str__(self):
        return str(self.username)
    
    class Meta:
        verbose_name = "Użytkownik"
        verbose_name_plural = "Użytkownicy"