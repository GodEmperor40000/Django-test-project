from django.urls import path
from .endpoint import views, auth_views

app_name = 'custom_user'
urlpatterns = [
    path('', auth_views.google_login),
    path('registration', views.registration, name='registration'),
    path('registration_creator', views.registration_creator, name='registration_creator'),
]