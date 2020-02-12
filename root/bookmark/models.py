from django.db import models


# Create your models here.
class Bookmark(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.title
