from django.db import models
from django.db.models import ImageField
from shortuuidfield import ShortUUIDField
from django.utils import timezone
import uuid
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser
from django.db.models.signals import post_save
from payments.models import Payment
from django_countries.fields import CountryField
from .validators import validate_file
from django.urls import reverse


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password=None)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    username = models.CharField(unique=True, max_length=40)
    user_id = models.AutoField(primary_key=True, auto_created=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = MyUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Profile(models.Model):
    STATUS_CHOICES = (
        ('h', 'Happy'),
        ('s', 'Sad'),
        ('b', 'Busy'),
        ('a', 'Available'),
        (',', 'Motivate'),
        ('l', 'Love'),
    )
    EXPERT_CHOICES = (
        ('s', 'Singer'),
        ('m', 'Musician'),
        ('p', 'Poet'),
        ('o', 'Others'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='avatars/', blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    expert = models.CharField(max_length=10, choices=EXPERT_CHOICES, default=3)
    nationality = CountryField()


def save_profile_user(sender, **kwargs):
    if kwargs['created']:
        profile_user = Profile(user=kwargs['instance'])
        profile_user.save()


post_save.connect(save_profile_user, sender=User)


class Post_user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=40)
    description = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('account:login')


class Images(models.Model):
    post = models.ForeignKey(Post_user, on_delete=models.CASCADE, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='Images/', null=True, blank=True)

    def __str__(self):
        return str(self.thumbnail)


class Videos(models.Model):
    post = models.ForeignKey(Post_user, on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(upload_to='videos/', null=True, blank=True)

    def __str__(self):
        return str(self.file)


class Voices(models.Model):
    post = models.ForeignKey(Post_user, on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(upload_to='Voices/', null=True, blank=True)

    def __str__(self):
        return str(self.file)


class Files(models.Model):
    post = models.ForeignKey(Post_user, on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(upload_to='Files/', null=True, blank=True)

    def __str__(self):
        return str(self.file)


class Post_like(models.Model):
    user = models.ForeignKey(User, related_name='user', blank=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post_user, related_name='posts', blank=True, on_delete=models.CASCADE)


class User_Follow(models.Model):
    self_id = models.ForeignKey(User, related_name='follower', blank=True, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, related_name='following', blank=True, on_delete=models.CASCADE)


class Post_comment(models.Model):
    user_id = models.ForeignKey(User, related_name='users', blank=True, on_delete=models.CASCADE)
    comment_id = models.ForeignKey("self", related_name='comment', blank=True, on_delete=models.CASCADE,null=True)
    post_id = models.ForeignKey(Post_user, related_name='post', blank=True, on_delete=models.CASCADE)
    description = models.TextField(max_length=300)