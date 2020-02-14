from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from . import fields


# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField('One Line Description', max_length=100)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('photo:album_detail', args=(self.id, ))

    def __str__(self):
        return self.name


class Photo(models.Model):
    title = models.CharField(max_length=50, blank=True)
    description = models.CharField('Photo Description', max_length=100, blank=True)
    upload_date = models.DateTimeField('Upload Date', auto_now_add=True)
    image = fields.ThumbnailImageField()
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=(self.id, ))

    def __str__(self):
        return self.title


