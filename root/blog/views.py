from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView
from django.views.generic.edit import FormView
from tagging.views import TaggedObjectList
from .models import Post
from .forms import PostSearchForm
from django.contrib.auth.decorators import login_required

''' 
login_required() 메서드는 로그인이 필요한 경우 로그인 페이지로 리다이렉트 지원
클래스 형 뷰에서는 함수형 테코레이터를 사용할 수 없기 때문에 클래스 정의 필요
classmethod() 형의 as_view()에서 login_required() 메서드가 실행되도록 한다
'''
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


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


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'description', 'content', 'tag']
    # initial = {'slug': 'auto-filling-do-not-input'}
    success_url = reverse_lazy('blog:post_index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostChangeLV(LoginRequiredMixin, ListView):
    template_name = 'blog/post_change_list.html'

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'description', 'content', 'tag']
    success_url = reverse_lazy('blog:post_index')


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_index')