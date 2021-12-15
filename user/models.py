from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

# Create your models here.
    
class Guest(User):
    class Meta:
        verbose_name = 'Guest'

    expired_date = models.DateField(null=True)
    date_of_birth = models.DateField(null=True)
    license = models.ImageField(upload_to='licenses', null=True)

    @property
    def thumbnail_license(self):
        if self.license:
            return mark_safe('<img src="{}" />'.format(self.license.url))
        return ""

