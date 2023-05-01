from django.contrib import admin
from .models import MenuItem

# Register your models here.


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'url')
    list_filter = ('parent',)
    search_fields = ('title', 'url')


admin.site.register(MenuItem, MenuItemAdmin)
