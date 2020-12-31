from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    db_name='postsdatabase'
    title = models.CharField(max_length=100)
    content = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='Post')
    def __str__(self):
        return str(self.title)
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})
    
    