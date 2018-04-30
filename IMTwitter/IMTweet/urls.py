from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('dashboard/', views.dashboard , name='dashboard'),
    # path('dashboard/', views.post_list , name='post_list'),
    # path('', views.index, name='index'),
]
