from django.db import models
from django.contrib.auth.models import User
from shortuuidfield import ShortUUIDField
from django.urls import reverse
from payments.models import Payment
from django.utils import timezone
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class MyUserManager(BaseUserManager):
    def create_user(self, email,username , uuid ,  password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')


        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,  email,username , uuid ,  password=None):
        user = self.create_user(
            email, username, uuid, password=None
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
        email = models.EmailField(verbose_name='email address',max_length=255,unique=True,)
        uuid = ShortUUIDField(unique=True)
        username = models.CharField(unique=True,max_length=40)
        user_id=  models.AutoField(primary_key=True,auto_created=True)
        desc = models.TextField(blank=True)
        image = models.ImageField(upload_to='avatars/')
        is_active = models.BooleanField(default=True)
        is_admin = models.BooleanField(default=False)

        objects = MyUserManager()

        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['username','email']

        def __str__(self):
            return self.email

        def has_perm(self, perm, obj=None):
            return True

        def has_module_perms(self, app_label):
            return True

        @property
        def is_staff(self):
            return self.is_admin