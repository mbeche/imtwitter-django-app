from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post
from .models import Comment

# def index(request):
#     return HttpResponse("Hello, world. This is where you will soon be able to interact with a post interface.")
# Create your views here.

@login_required
def dashboard(request):
    posts = Post.objects.all().order_by('-pud_date')
    comments = Comment.objects.all()
    return render(request, 'dashboard.html', {'section': 'dashboard', 'posts':posts, 'comments':comments})

def post_list(request):
    return render(request, 'post_list.html', {})
