from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. This is where you will soon be able to interact with a post interface.")
# Create your views here.
