from django.urls import path, re_path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('dashboard/', views.dashboard , name='dashboard'),
    re_path(r'^post_comment_on_(?P<pk>\d+)/?', views.add_comment_to_post , name='add_comment_to_post'),
    # path('dashboard/', views.post_list , name='post_list'),
    # path('', views.index, name='index'),
]
