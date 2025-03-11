from django.contrib import admin
from .models import Craftsman

class CraftsmanAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'service', 'photo_preview')
    list_filter = ('service',)
    search_fields = ('first_name', 'last_name', 'user__username', 'service__title')
    fields = ('user', 'first_name', 'last_name', 'photo', 'service', 'bio', 'address')
    readonly_fields = ('photo_preview',)

    def photo_preview(self, obj):
        if obj.photo:
            return f'<img src="{obj.photo.url}" style="width: 100px; height: auto;" />'
        return "No photo"
    photo_preview.allow_tags = True
    photo_preview.short_description = 'Photo Preview'

admin.site.register(Craftsman, CraftsmanAdmin)