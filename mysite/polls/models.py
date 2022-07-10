import datetime
from tabnanny import verbose
from django.contrib import admin
from django.db import models
from django.utils import timezone




class Question(models.Model):
    ist_filter = ['pub_date']
    search_fields = ['question_text']
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Дата публикации')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Опубликовано недавно?',    
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'



