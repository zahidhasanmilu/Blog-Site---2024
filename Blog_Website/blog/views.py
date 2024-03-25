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
# from App_account.models import User, Profile
# from App_shop.models import Product, Category,ProductImage

# forms
# from App_account.forms import SignUpForm

# message
from django.contrib import messages

import uuid
from django.db.models import Q


######################## Create your views here. #############################
def home(request):
    return render(request, 'home.html')


def blogs(request):
    return render(request, 'blogs.html')