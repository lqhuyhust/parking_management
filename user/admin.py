from django.contrib import admin
from .models import Guest, Security, GuestType
# Register your models here.
class GuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'is_active', )
    readonly_fields = ('thumbnail_license',)

    def thumbnail_license(self, obj):
        return obj.thumbnail_license

    thumbnail_license.short_description = 'License Image'
    thumbnail_license.allow_tags = True

    search_fields = ('username', 'first_name')
    list_filter  = ('is_active', )

admin.site.register(Guest, GuestAdmin)

class SecurityAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'car_park', 'port', )
    search_fields = ('username', 'first_name')
    list_filter  = ('car_park', )
admin.site.register(Security, SecurityAdmin)

class GuestTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fee', )
admin.site.register(GuestType,GuestTypeAdmin)
