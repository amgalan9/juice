from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    author = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile.jpg', upload_to='profile_pics')
