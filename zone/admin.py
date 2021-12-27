from django.contrib import admin
from .models import Zone

# Register your models here.
admin.site.site_header = 'Car Park: X20'
class ZoneAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'floor', 'data', 'number')
    search_fields = ('__str__', )
    list_filter  = ('floor', )
admin.site.register(Zone, ZoneAdmin)