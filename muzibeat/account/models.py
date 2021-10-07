from django.db import models
from shortuuidfield import ShortUUIDField
from django.utils import timezone
import uuid
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser
from django.db.models.signals import post_save





class MyUserManager(BaseUserManager):
    def create_user(self,email,username,password):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(email=self.normalize_email(email),username=username)
        user.set_password(password)
        return user

    def create_superuser(self,email,username,password):
        user = self.create_user(email,username,password=None)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
        email = models.EmailField(verbose_name='email address',max_length=255,unique=True)
        uuid = models.UUIDField(default=uuid.uuid4 ,editable=False)
        username = models.CharField(unique=True,max_length=40)
        user_id = models.AutoField(primary_key=True,auto_created=True)
        desc = models.TextField(blank=True)
        image = models.ImageField(upload_to='avatars/')
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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True)

def save_profile_user(sender, **kwargs):
    if kwargs['created']:
        profile_user = Profile(user= kwargs['instance'])
        profile_user.save()


post_save.connect(save_profile_user, sender=User)