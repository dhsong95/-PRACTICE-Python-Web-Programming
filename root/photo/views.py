from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Album, Photo


# Create your views here.
class AlbumLV(ListView):
    model = Album


class AlbumDV(DetailView):
    model = Album


class PhotoDV(DetailView):
    model = Photo