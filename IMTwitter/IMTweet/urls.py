from django.urls import path, re_path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('dashboard/', views.dashboard , name='dashboard'),
    path('addpost/', views.add_post, name='add_post'),
    re_path(r'^post_comment_on_(?P<pk>\d+)/?', views.add_comment_to_post , name='add_comment_to_post'),
    re_path(r'^edit-post/(?P<pk>\d+)/$', views.edit_post, name='edit_post'),
    re_path(r'^edit-comment/(?P<pk>\d+)/$', views.edit_comment, name='edit_comment'),
    re_path(r'^delete-post/(?P<pk>\d+)/$', views.delete_post, name='delete_post'),
    re_path(r'^delete-comment/(?P<pk>\d+)/$', views.delete_comment, name='delete_comment'),
]
