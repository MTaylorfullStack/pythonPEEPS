from django.db import models


class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Message(models.Model):
    message = models.CharField(max_length=100)
    poster = models.ForeignKey(User, related_name='all_messages', on_delete = models.CASCADE)
    users_who_liked = models.ManyToManyField(User, related_name='liked_messages')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
# Create your models here.
