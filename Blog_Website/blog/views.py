from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect, HttpResponse
from django.urls import reverse, reverse_lazy

# VIEW
from django.views.generic import CreateView, ListView, DetailView, UpdateView, View, TemplateView, DeleteView

# Authentication
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# forms
from django.contrib.auth.forms import AuthenticationForm

# models
from blog.models import Blog,Tag, Category, Comment
# from App_shop.models import Product, Category,ProductImage

# forms
# from App_account.forms import SignUpForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# message
from django.contrib import messages

import uuid
from django.db.models import Q


######################## Create your views here. #############################
def home(request):
    blogs = Blog.objects.all().order_by('-created_date')
    tags = Tag.objects.all().order_by('-created_date')
    
    context={
        'blogs':blogs,
        'tags':tags
    }
    return render(request, 'home.html',context)


def blogs(request):
    queryset = Blog.objects.all().order_by('-created_date')
    tags = Tag.objects.all().order_by('-created_date')
    #paginator
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 2)
    
    try:
        # Get the objects for the requested page
        blogs = paginator.page(page)    
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blogs = paginator.page(1)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogs = paginator.page(1)
        return redirect('blogs')
    

    context={
        'blogs':blogs,
        'tags':tags,
        'paginator':paginator,
    }
    return render(request, 'blogs.html',context)