from django.contrib import admin
from django.utils.safestring import mark_safe

from unfold.admin import ModelAdmin as UnfoldModelAdmin, StackedInline
from unfold.decorators import display

from ..models import Place, PlaceImage


class PlaceImageInline(StackedInline):
    model = PlaceImage
    extra = 1
    readonly_fields = ['preview']

    def preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" height="100" style="border-radius: 8px;" />')
        return ''
    preview.short_description = 'Превью'


@admin.register(Place)
class PlaceAdmin(UnfoldModelAdmin):
    list_display = ['name', 'category', 'rating', 'display_photo']
    list_filter = ['category', 'rating']
    search_fields = ['name', 'description']
    inlines = [PlaceImageInline]

    @display(description="Фото")
    def display_photo(self, obj):
        if obj.photo:
            return mark_safe(
                f'<img src="{obj.photo.url}" height="120" width="120" '
                f'style="border-radius: 10%;" />')
