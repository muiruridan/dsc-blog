from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog


# Create your views here.


def home(request):
    return render(request, "blog/index.html")


def blog(request):
    return render(request, "blog/blog.html")


def blog_details(request):
    return render(request, "blog/blog-details.html")
