from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Extends user model, one-to-one relationship
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=128)

    @property
    def user_profile(self):
        context = {'username': self.user.username}
        return context
    
