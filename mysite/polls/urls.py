from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('polls/add_new_poll', views.add_new_poll, name = 'add_new_poll'),
    path('polls/create_poll', views.create_poll, name = 'create_poll'),
    #path('polls/num_of_choices', views.num_of_choices, name = 'num_of_choices'),
    path('polls/prom_zv_1', views.prom_zv_1, name = 'prom_zv_1'),
]