from asyncio.windows_events import NULL
from django.shortcuts import render
from django.http import HttpResponse
from django.http import  Http404, HttpResponseRedirect
from users_account.models import Custom_user
from django.urls import reverse
from django.db import models
from django.utils import timezone
from datetime import datetime

def registration_creator(request):
    return render(request, 'auth/registration.html')

def registration(request):
    Custom_user.objects.create(
        username = request.POST['name'], 
        password = request.POST['password'], 
        email_user = request.POST['email'],
        join_date = datetime.now(),
        user_bio = request.POST['bio'],
        user_avatar = request.POST['avatar'],
        )
    return render(request, 'homepage/list.html')
