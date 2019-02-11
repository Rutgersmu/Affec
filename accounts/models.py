from django.conf import settings
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

username_validator = UnicodeUsernameValidator()
class User(AbstractUser):
    is_affector = models.BooleanField(default=False)
    name = models.CharField(max_length=20, verbose_name='이름')
    nickname = models.CharField(max_length=20, verbose_name='nickname')



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    tag = models.CharField(max_length=50)
    email = models.EmailField()


def on_post_save_for_user(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        Profile.objects.create(user=user);


post_save.connect(on_post_save_for_user, sender=settings.AUTH_USER_MODEL)

class Desc(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    content = models.TextField()









# Create your models here.
