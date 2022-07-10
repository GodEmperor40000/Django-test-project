from asyncio.windows_events import NULL
from django.shortcuts import render
from django.http import HttpResponse
from django.http import  Http404, HttpResponseRedirect
from .models import Article, Coment
from django.urls import reverse
from django.db import models
from django.utils import timezone
from datetime import datetime

def index(request):
    all_articles_list = Article.objects.all()
    latest_articles_list = Article.objects.order_by('-pub_date')[:1]
    return render(request, 'articles/list.html',{'all_articles_list': all_articles_list, 'latest_articles_list' : latest_articles_list})

def detail(request, article_id):
    try:
        a = Article.objects.get( id = article_id)
    except:
        raise Http404("No article!")

    latest_comments_list = a.coment_set.order_by('-id')[:10]

    return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list':latest_comments_list })

def add_article(request):
    #new_article = Article.create(article_title = request.POST['title'], article_text = request.POST['text'], pub_date = datetime.now())
    cur2_date = datetime.now()
    #cur_date = bytes(datetime.datetime.now())
    Article.objects.create(article_title = request.POST['title'], article_text = request.POST['text'], pub_date =cur2_date)

    return render(request, 'homepage/list.html')

def create_article(request):
    return render(request, 'articles/add_article.html')

def leave_comment(request, article_id):
    try:
        a = Article.objects.get( id = article_id)
    except:
        raise Http404("No article!")

    a.coment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

    return HttpResponseRedirect( reverse('articles:detail', args = (a.id,)))