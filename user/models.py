from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

# Create your models here.
    
class Guest(User):
    class Meta:
        verbose_name = 'Guest'

    phone = models.CharField(null=True, max_length=12)
