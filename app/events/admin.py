from django.contrib import admin
from django.utils.safestring import mark_safe
from unfold.admin import ModelAdmin as UnfoldModelAdmin
from unfold.decorators import display

from .models import Event


@admin.register(Event)
class EventAdmin(UnfoldModelAdmin):
    list_display = ('title', 'location', 'start_date', 'is_published', 'display_photo')
    list_filter = ('is_published', 'start_date')
    search_fields = ('title', 'location', 'description')

    @display(description="Фото")
    def display_photo(self, obj):
        if obj.photo:
            return mark_safe(
                f'<img src="{obj.photo.url}" height="120" width="120" '
                f'style="border-radius: 10%;" />')
