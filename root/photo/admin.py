from django.contrib import admin
from .models import Album, Photo


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 2


class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    inlines = [PhotoInline]


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'upload_date']


# Register your models here.
admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
