from django.urls import path

from . import views
from django.urls import include

urlpatterns = [
    path('', views.index, name = 'index'),
    path('articles/', include('articles.urls')),
    path('polls/', include('polls.urls')),
]