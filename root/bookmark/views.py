from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from .models import Bookmark

# Create your views here.

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



class BookmarkLV(ListView):
    model = Bookmark


class BookmarkDV(DetailView):
    model = Bookmark


class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:bookmark_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BookmarkCreateView, self).form_valid(form)


class BookmarkChangeLV(LoginRequiredMixin, ListView):
    template_name = 'bookmark/bookmark_change_list.html'

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)


class BookmarkUpdateView(LoginRequiredMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:bookmark_list')


class BookmarkDeleteView(LoginRequiredMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:bookmark_list')
