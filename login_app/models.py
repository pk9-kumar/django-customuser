from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .managers import UserManager


class User(AbstractUser, PermissionsMixin):
    username = None

    phone = models.CharField(verbose_name='Phone', max_length=10, unique=True)
    otp = models.CharField(verbose_name='otp', max_length=6)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['otp']

    objects = UserManager()

    def __str__(self):
        return self.phone


class City(models.Model):
    city = models.CharField('City', max_length=25)

    def __str__(self):
        return self.city


class UserCity(models.Model):
    user = models.OneToOneField(User, related_name='user_city', on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.city)

