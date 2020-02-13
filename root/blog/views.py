from django.shortcuts import render
from django.db.models import Q
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView
from django.views.generic.edit import FormView
from tagging.views import TaggedObjectList
from .models import Post
from .forms import PostSearchForm


# Create your views here.
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2


class PostDV(DetailView):
    model = Post


class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'


class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_date'
    make_object_list = True


class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_date'


class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_date'


class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'


class TagTV(TemplateView):
    template_name = 'tagging/tag_cloud.html'


class PostTOL(TaggedObjectList):
    model = Post
    template_name = 'tagging/tagged_object_list.html'


class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        search_word = form.cleaned_data['search_word'] if form.is_valid() else None
        object_list = Post.objects.filter(
            Q(title__icontains=search_word) |
            Q(description__icontains=search_word) |
            Q(content__icontains=search_word)).distinct()

        context = dict()
        context['form'] = form
        context['search_word'] = search_word
        context['object_list'] = object_list

        return render(self.request, self.template_name, context)
