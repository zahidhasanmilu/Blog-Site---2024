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
from blog.models import Blog, Tag, Category, Comment, Reply
# from App_shop.models import Product, Category,ProductImage

# forms
from blog.forms import TextForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# message
from django.contrib import messages

import uuid
from django.db.models import Q


######################## Create your views here. #############################
def home(request):
    blogs = Blog.objects.all().order_by('-created_date')
    tags = Tag.objects.all().order_by('-created_date')

    context = {
        'blogs': blogs,
        'tags': tags
    }
    return render(request, 'home.html', context)


def blogs(request):
    queryset = Blog.objects.all().order_by('-created_date')
    tags = Tag.objects.all().order_by('-created_date')
    # paginator
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

    context = {
        'blogs': blogs,
        'tags': tags,
        'paginator': paginator,
    }
    return render(request, 'blogs.html', context)


def catagory_blog(request, slug):
    category = get_object_or_404(Category, slug=slug)
    blogs = category.category_blogs.all()
    tags = Tag.objects.all().order_by('-created_date')

    context = {
        'category': category,
        'blogs': blogs,
        'tags': tags
    }
    return render(request, 'category_blogs.html', context)


def tag_blogs(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    blogs = tag.tag_blogs.all()
    tags = Tag.objects.exclude(slug=slug).order_by('-created_date')
    # tags = Tag.objects.all().order_by('-created_date')

    context = {
        'tag': tag,
        'blogs': blogs,
        'tags': tags
    }
    return render(request, 'tag_blogs.html', context)


def blog_details(request, slug):
    # Retrieve the blog post
    blog = get_object_or_404(Blog, slug=slug)

    # Retrieve related blogs based on the category of the current blog
    related_blogs = Blog.objects.filter(
        category=blog.category).exclude(slug=slug)[:3]

    # Retrieve all tags
    tags = blog.tags.all().order_by('-created_date')

    # Initialize an empty form for comments
    form = TextForm()

    # Handle form submission for adding comments
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            # Create a new comment associated with the blog post
            Comment.objects.create(
                user=request.user,
                blog=blog,
                text=form.cleaned_data.get('text')
            )
            # Redirect to the same blog post page after successful submission
            return redirect('blog_details', slug=slug)

    # Prepare context to be passed to the template
    context = {
        'blog': blog,
        'tags': tags,
        'related_blogs': related_blogs,
        'form': form
    }

    # Render the template with the provided context
    return render(request, 'post-details.html', context)


def add_reply(request, blog_id, comment_id):
    blog = get_object_or_404(Blog, id=blog_id)
    comment = get_object_or_404(Comment, id=comment_id)

    form = TextForm()

    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            Reply.objects.create(
                user=request.user,
                text=form.cleaned_data.get('text'),
                comment=comment
            )

    return redirect('blog_details', slug=blog.slug)


def search_blog(request):
    recent_blogs = Blog.objects.order_by('-created_date')
    tags = Tag.objects.order_by('-created_date')

    search_item = request.GET.get('search')
    
    print(search_item)
    if search_item:
        blogs = Blog.objects.filter(
            Q(title__icontains=search_item) 
          
        )
        context = {
            "blogs": blogs,
            "recent_blogs": recent_blogs,
            "tags": tags,
            "search_item": search_item
        }
        return render(request, 'search.html', context)
    # if search_item:
    #     blogs = Blog.objects.filter(
    #         Q(title__icontains=search_item) |
    #         Q(category__title__icontains=search_item) |
    #         Q(user__username__icontains=search_item) |
    #         Q(tags__title__icontains=search_item)
    #     ).distinct()

    #     context = {
    #         "blogs": blogs,
    #         "recent_blogs": recent_blogs,
    #         "tags": tags,
    #         "search_item": search_item
    #     }
    #     return render(request, 'search.html', context)
