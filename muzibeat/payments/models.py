from django.db import models
from django.utils import timezone


# Create your models here.
class Payment(models.Model):
    status_choices = (
        ('d', 'Done'),
        ('f', 'Failed'),
        ('s', 'Suspended'),
    )
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    price = models.CharField(max_length=40)
    ref = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices=status_choices)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.status
