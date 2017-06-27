# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request, id):
    instance = get_object_or_404(Post, id=id)
    context = {
        "Title": instance.title,
        "instance": instance
    }
    return render(request, "post_detail.html", context)

def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None )
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    #else:
    #    messages.error(request, "Not Successfully Created")
    #if request.method == "POST":
    #    print request.POST.get("content")
    #    print request.POST.get("title")
    context = {
        "form": form
    }
    return render(request, "post_form.html", context)

def post_list(request):
    queryset_list = Post.objects.all()#.order_by("-timestamp")
    paginator = Paginator(queryset_list,5)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "Title": "List",
        "page_request_var": page_request_var,
    }
    return render(request, "post_list.html", context)

def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "Title": instance.title,
        "instance": instance,
        "form": form
    }
    return render(request, "post_form.html", context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Post Deleted successfully")
    return redirect("posts:list")