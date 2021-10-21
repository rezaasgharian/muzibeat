from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager


# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self,email,username,password):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(email=self.normalize_email(email),username=username)
        user.set_password(password)
        return user

    def create_superuser(self,email,username,password):
        user = self.create_user(email,username,password=None)
        user.is_admin = True
        user.save(using=self._db)
        return user



class Post_admin(models.Model):
    user = models.ForeignKey(MyUserManager, on_delete=models.CASCADE,null=True, blank=True)
    title = models.CharField(max_length=40)
    description = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Images(models.Model):
    post = models.ForeignKey(Post_admin, on_delete=models.CASCADE,null=True, blank=True)
    thumbnail = models.ImageField(upload_to='Images/')
class Videos(models.Model):
    post = models.ForeignKey(Post_admin, on_delete=models.CASCADE,null=True, blank=True)
    file = models.FileField(upload_to='videos/')
class Voices(models.Model):
    post = models.ForeignKey(Post_admin, on_delete=models.CASCADE,null=True, blank=True)
    file = models.FileField(upload_to='Voices/')
class Files(models.Model):
    post = models.ForeignKey(Post_admin, on_delete=models.CASCADE,null=True, blank=True)
    file = models.FileField(upload_to='Files/')



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

    def __str__(self):
        return self.title