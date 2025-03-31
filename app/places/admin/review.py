from django.contrib import admin

from unfold.admin import ModelAdmin as UnfoldModelAdmin

from ..models import Review


@admin.register(Review)
class ReviewAdmin(UnfoldModelAdmin):
    list_display = ['place', 'user', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['text', 'user__username']
