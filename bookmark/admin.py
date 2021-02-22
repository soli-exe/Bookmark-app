from django.contrib import admin
# from django.contrib import admin
from .models import BookMark


@admin.register(BookMark)
class BookmarksAdmin(admin.ModelAdmin):
    list_display = ['bookmark_title', 'bookmark_publication_date']
