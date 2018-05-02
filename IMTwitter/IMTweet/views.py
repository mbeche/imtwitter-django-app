from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from .models import Post
from .models import Comment
from .forms import PostForm, CommentForm
from django.utils import timezone
from django.shortcuts import redirect

# def index(request):
#     return HttpResponse("Hello, world. This is where you will soon be able to interact with a post interface.")
# Create your views here.

@login_required
def dashboard(request):
    posts = Post.objects.all().order_by('-pud_date')
    comments = Comment.objects.all().order_by('-pud_date')
    return render(request, 'dashboard.html', {'section': 'dashboard', 'posts':posts, 'comments':comments})

@login_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pud_date = timezone.now()
            post.user = request.user
            post.save()
            return redirect('dashboard')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.pub_date = timezone.now()
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('dashboard')
        else:
            form = CommentForm()
            return render(request, 'add_comment_to_post.html', {'form': form, 'post':post})

def user_author_check(author, user):
    return author == user

@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user_auth = user_author_check(post.user, request.user)
    if user_author_check(post.user, request.user):
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form = PostForm(instance=post)
        return render(request, 'add_post.html', {'form': form, 'post': post, 'user_auth': user_auth})
    else:
        return HttpResponse("You do not have permission to edit this post.")

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if user_author_check(post.user, request.user):
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            post.delete()
            return redirect('dashboard')
        else:
            form = PostForm(instance=post)
        return render(request, 'add_post.html', {'form': form, 'post': post})
    else:
        return HttpResponse("You do not have permission to delete this post.")

# @login_required
# def delete_comment(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     if user_author_check(comment.user, request.user):
#         if request.method == "POST":
#             form = CommentForm(request.POST, instance=comment)
#             post.delete()
#             return redirect('dashboard')
#         else:
#             form = PostForm(instance=post)
#         return render(request, 'add_post.html', {'form': form, 'post': post})
#     else:
#         return HttpResponse("You do not have permission to delete this post.")

@login_required
def edit_comment(request, pk):
    return
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False, instance=comment)
#             comment.pub_date = timezone.now()
#             comment.user = request.user
#             comment.post = post
#             comment.save()
#             return redirect('dashboard')
#         else:
#             form = CommentForm()
#             return render(request, 'add_comment_to_post.html', {'form': form, 'post':post})
#     comment = get_object_or_404(Comment, pk=pk)
#     if request.method == "POST":
#         form = CommentForm(request.POST, instance=comment)
#         if form.is_valid():
#             form.save()
#     else:
#         form = PostForm(instance=comment)
#     return render(request, 'add_comment_to_post.html', {'form': form, 'comment': comment})
