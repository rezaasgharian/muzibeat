from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from django.db import models


# Create your models here.
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )


class Artist(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    thumbnail = models.ImageField(upload_to='images/', blank=False)


class Album(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=250, null=True, blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='images/', blank=False)


class Song(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=250, null=True, blank=True)
    artist = models.ForeignKey(Artist, null=False, blank=False, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, null=True, blank=True, on_delete=models.CASCADE)
    song = models.FileField(upload_to='musics/', null=False, blank=False)
    thumbnail = models.ImageField(upload_to='images/', blank=False)