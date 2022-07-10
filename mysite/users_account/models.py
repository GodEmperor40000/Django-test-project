import datetime
from tkinter import CASCADE
from wsgiref.validate import validator
from django.core.validators import FileExtensionValidator
from distutils.command.upload import upload
from hashlib import blake2b
from socket import errorTab
from tabnanny import verbose
from django.db import models
from django.forms import CharField
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from base.services import get_path_upload_avatar, validate_size_avatar
from PIL import Image
 
class Custom_user(models.Model):
    username = models.TextField('Имя пользователя')
    password = models.TextField('Пароль пользователя')
    
    email_user = models.EmailField(unique=True)
    join_date = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=30, null = True)
    user_bio = models.TextField(max_length = 200000, blank = True, null = True)
    user_avatar  = models.ImageField(
        upload_to = get_path_upload_avatar,
        blank = True, 
        null = True,
        validators = [FileExtensionValidator(allowed_extensions=['png', 'jpg']), validate_size_avatar]
        )
    pass

    def __str__(self):
        return self.email_user

    @property
    def is_authorized(self):
        return True

class Follower(models.Model):

    user = models.ForeignKey(Custom_user, on_delete=models.CASCADE, related_name='owner')
    subscriber = models.ForeignKey(Custom_user, on_delete=models.CASCADE, related_name='subscriber')

    def __str__(self):
        return f'{self.subscriber} читает {self.user}'
