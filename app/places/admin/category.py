from django.contrib import admin
from django.utils.safestring import mark_safe

from unfold.admin import ModelAdmin as UnfoldModelAdmin
from unfold.decorators import display

from ..models import Category


@admin.register(Category)
class CategoryAdmin(UnfoldModelAdmin):
    list_display = ['name', 'description', 'display_icon']
    search_fields = ['name']

    @display(description="Фото")
    def display_icon(self, obj):
        if obj.icon:
            return mark_safe(
                f'<img src="{obj.icon.url}" height="120" width="120" '
                f'style="border-radius: 10%;" />')