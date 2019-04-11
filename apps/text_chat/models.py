from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ChatGroup(models.Model):
    group_name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    group_creator = models.OneToOneField(User, models.CASCADE)
    participants = models.ManyToManyField(User, related_name='chat_group_participants')

    def __str__(self):
        return self.group_name
