from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):

    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )

    title = models.CharField(max_length=40)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='PostImages/')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)







# class concertModel(models.Model):
#     Name = models.CharField(max_length=40)
#     SingerName = models.CharField(max_length=40)
#     Lenght = models.IntegerField()
#     Poster = models.ImageField(upload_to='concertImage/',null=True)
#
#     def __str__(self):
#         return self.SingerName
