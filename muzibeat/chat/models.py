from django.db import models
from django.conf import settings


# Create your models here.

class Chat(models.Model):
    roomname = models.CharField(blank=True, max_length=50)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self):
        return self.roomname


class Message(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    related_chat = models.ForeignKey(Chat, on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def last_message(self, roomname):
        return Message.objects.filter(related_chat__roomname=roomname)

    def __str__(self):
        return self.author.username
