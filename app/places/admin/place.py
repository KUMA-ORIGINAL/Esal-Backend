from django.contrib import admin
from django.utils.safestring import mark_safe

from unfold.admin import ModelAdmin as UnfoldModelAdmin
from unfold.decorators import display

from ..models import Place


@admin.register(Place)
class PlaceAdmin(UnfoldModelAdmin):
    list_display = ['name', 'category', 'rating', 'address', 'display_photo']
    list_filter = ['category', 'rating']
    search_fields = ['name', 'description']

    @display(description="Фото")
    def display_photo(self, obj):
        if obj.photo:
            return mark_safe(
                f'<img src="{obj.photo.url}" height="120" width="120" '
                f'style="border-radius: 10%;" />')
