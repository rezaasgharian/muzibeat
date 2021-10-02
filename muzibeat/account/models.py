from django.db import models
from django.contrib.auth.models import User
from shortuuidfield import ShortUUIDField
from django.urls import reverse
from payments.models import Payment
from django.utils import timezone
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UserRegister(models.Model):
    uuid = ShortUUIDField(unique=True)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='avatars/')
    class Meta:
        verbose_name_plural = 'accounts'

    def __unicode__(self):
        return u"%s" % self.name


    def get_absolute_url(self):
        return 'account_detail',[self.uuid]


    def get_update_url(self):
        return 'account_update', [self.uuid]


    def get_delete_url(self):
        return 'account_delete', [self.uuid]

