from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    published_date=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"title:{self.title} author:{self.author}"

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})