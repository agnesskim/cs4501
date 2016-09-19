from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User

#from datetime import datetime

#from django.db.models import Count, Min, Sum, Avg, Max


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
         self.published_date = timezone.now()
         self.save()

    def __str__(self):
         return self.title

class User(models.Model):
     username = models.CharField(max_length=25, unique=True)
     password = models.CharField(max_length=100)
     first_name = models.CharField(max_length=20)
     last_name = models.CharField(max_length=20)

class Comment(models.Model):
     post = models.ForeignKey(Post)
     message = models.TextField()
     created_date = models.DateTimeField(default=timezone.now)