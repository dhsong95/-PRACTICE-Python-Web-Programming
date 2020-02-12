from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Bookmark


# Create your views here.
class BookmarkLV(ListView):
    model = Bookmark


class BookmarkDV(DetailView):
    model = Bookmark
