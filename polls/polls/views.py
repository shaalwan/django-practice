from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from . import models

def index(request):
    questions = models.Question.objects.all()[:5]
    return render(request, 'polls/index.html',{'questions':questions})

def question(request, question_id):
    ques = get_object_or_404(models.Question, pk = question_id)
    return render(request, 'polls/question.html',{'ques':ques})

def vote(request, question_id):
    question = get_object_or_404(models.Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, models.Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def result(request, question_id):
    ques = get_object_or_404(models.Question, pk = question_id)
    return render(request, 'polls/result.html',{'question':ques})