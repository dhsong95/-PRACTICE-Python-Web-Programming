from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required



class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_name'] = ['bookmark', 'blog']
        return context


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


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
