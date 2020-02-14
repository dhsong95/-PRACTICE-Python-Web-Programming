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
    path('tag/', views.TagTV.as_view(), name='tag_cloud'),
    re_path('tag/(?P<tag>[^/]+(?u))/$', views.PostTOL.as_view(), name='tagged_object_list'),
    path('search/', views.SearchFormView.as_view(), name='search'),
    path('add/', views.PostCreateView.as_view(), name='post_create'),
    path('change/', views.PostChangeLV.as_view(), name='post_change_list'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
