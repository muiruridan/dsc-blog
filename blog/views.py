from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

# Create your views here.


def home(request):
    blogs = Blog.objects.filter(name='1st Blog')
    q = blogs.query
    return HttpResponse(q)
