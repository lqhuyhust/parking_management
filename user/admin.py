from django.contrib import admin
from .models import Guest, Security, GuestType
# Register your models here.
class GuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'username', 'email', 'is_active', )
    readonly_fields = ('thumbnail_license',)

    def thumbnail_license(self, obj):
        return obj.thumbnail_license

    thumbnail_license.short_description = 'License Image'
    thumbnail_license.allow_tags = True

admin.site.register(Guest, GuestAdmin)
admin.site.register(Security)
admin.site.register(GuestType)
