from django.contrib import admin
from .models import Guest
# Register your models here.
class GuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'is_active', )

    search_fields = ('username', 'first_name')
    list_filter  = ('is_active', )

admin.site.register(Guest, GuestAdmin)

