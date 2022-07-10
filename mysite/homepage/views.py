from asyncio.windows_events import NULL
from django.shortcuts import render
from django.http import HttpResponse
from django.http import  Http404, HttpResponseRedirect
from articles.models import Article, Coment
from django.urls import reverse
from django.db import models

def index(request):

    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1  

    return render(request, 'homepage/list.html', {'num_visits': num_visits})
