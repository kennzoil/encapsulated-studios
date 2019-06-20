# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import RequestContext, Template
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template.context_processors import csrf
from django.db import connection, transaction
from django.urls import reverse_lazy
from django.views import generic
from .api import *
from .forms import *
from .models import *
import json

@csrf_protect
def render_homepage(request):
    """ render when homepage is requested """

    """ authenticate newly registered user"""
    if request.method == 'POST':

        # authenticate newly registered user
        if 'username' in request.POST:
            
            pass

            # form = CustomUserCreationForm(request.POST)
            #
            # if form.is_valid():
            #     new_user = form.save()
            #     new_user = authenticate(
            #         username=form.cleaned_data['username'],
            #         password=form.cleaned_data['password1'],
            #     )
            #     login(request, new_user)


    """ retrieve stuff for homepage view """
    # news_posts = get_news_items()
    # news_post_comments = NewsItemComment.objects.all()

    """ bundle into contexst for page render """
    context = {
        "csrf": csrf,
    }

    return render(request, 'index.html', context)