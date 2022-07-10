from datetime import date
from random import choices
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from datetime import datetime

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
       
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Выбери выбор, товарищ!",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

#Принимат данные add_new_poll
def add_new_poll(request):
    ch_text = {}
    cur_date = datetime.now()
    choices = request.session.get('choices') #колиество вариантов ответа
    question1 = Question.objects.create(question_text = request.POST['text'], pub_date = cur_date ) #создание экземпляра вопроса
    ch_text = request.POST.getlist('ch_text')
    for i in range(choices):
        
        Choice.objects.create(question = question1, choice_text = ch_text[i])
    
    return render(request, 'homepage/list.html')

#Формирует add_new_poll
def prom_zv_1(request):
    all_choices = int(request.POST.get('num', 0))
    if all_choices <= 0:
        return render(request, 'polls/num_of_choices.html', {'error_message': "Поворот не туда", 'err_num': all_choices})
    else:
        choices = request.session.get('choices')
        request.session['choices'] = all_choices 
        num_of_all_choices = [i for i in range(all_choices)]
        return render(request, 'polls/add_new_poll.html', {'all_choices': num_of_all_choices, 'num_choices': all_choices, 'session': choices})
        
        


#Формирует num_of_choices
def create_poll(request):
    return render(request, 'polls/num_of_choices.html')