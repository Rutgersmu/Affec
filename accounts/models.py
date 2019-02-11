from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    is_affector = models.BooleanField(default=False)
    name = models.CharField(max_length=20)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50)
    email = models.EmailField()


class Desc(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    content = models.TextField()









# Create your models here.
