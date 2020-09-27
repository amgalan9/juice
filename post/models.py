from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

class Post(models.Model):
    "class for Post/Project entry in the Post app"

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(default='default.jpg', upload_to='thumbnails')