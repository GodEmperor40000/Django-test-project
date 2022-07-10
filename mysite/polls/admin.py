from django.contrib import admin

from .models import Choice, Question
from users_account import models


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')


admin.site.register(Question, QuestionAdmin)

@admin.register(models.Custom_user)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email_user', 'join_date')
    list_display_links = ('email_user',)