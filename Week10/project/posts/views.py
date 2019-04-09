# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Posts
from django.http import HttpResponse

def index(request) :

    posts = Posts.objects.all()[:10]

    context = {
        'title' : 'Latest Posts',
        'posts' : posts
    }

    return render(request, 'posts/index.html', context)

def details(request,id) :
    posts = Posts.objects.get(id=id)

    context = {
        'posts': posts
    }
    return render(request, 'posts/details.html', context)