from django.contrib import admin
from .models import Car
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'guest', 'name', 'brand', 'color', 'license_plate', )
    readonly_fields = ('thumbnail_image', 'thumbnail_registration', )

    def thumbnail_registration(self, obj):
        return obj.thumbnail_registration

    thumbnail_registration.short_description = 'Registration Image'
    thumbnail_registration.allow_tags = True

    def thumbnail_image(self, obj):
        return obj.thumbnail_image

    thumbnail_image.short_description = 'Car Image'
    thumbnail_image.allow_tags = True

admin.site.register(Car, CarAdmin)