from django.contrib import admin
from .models import Bookmark


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']


# Register your models here.
admin.site.register(Bookmark, BookmarkAdmin)