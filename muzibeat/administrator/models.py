from django.db import models
from django.utils import timezone


# Create your models here.
class category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    status = models.BooleanField(default=True, )
    position = models.IntegerField()

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.title


class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )

    title = models.CharField(max_length=40)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    category = models.ManyToManyField(category, related_name='post')
    thumbnail = models.ImageField(upload_to='PostImages/')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title
