from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Bookmark(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(unique=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
