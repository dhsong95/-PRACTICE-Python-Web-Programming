from django.urls import path, re_path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostLV.as_view(), name='post_index'),
    path('post/', views.PostLV.as_view(), name='post_list'),
    re_path('post/(?P<slug>[-a-zA-Z0-9_ㄱ-힣]+)/$', views.PostDV.as_view(), name='post_detail'),
    path('archive/', views.PostAV.as_view(), name='post_archive'),
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_archive_year'),
    path('archive/<int:year>/<slug:month>/', views.PostMAV.as_view(), name='post_archive_month'),
    path('archive/<int:year>/<slug:month>/<int:day>/', views.PostDAV.as_view(), name='post_archive_day'),
    path('archive/today/', views.PostTAV.as_view(), name='post_archive_today'),
]
