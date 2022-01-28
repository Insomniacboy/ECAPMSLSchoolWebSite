from re import A
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from random import randint
from .models import Question


a: int
a=randint(0,100)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.html)
    context={
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)
#    return HttpResponse(template.render(context,request))
#    output = ', '.join([q.question_text for q in latest_question_list]) 
#    return HttpResponse("Congratulations! You sent your vote. " + str(randint(0, 10))) 

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        return render(request, 'polls/error404.html')
    return render(request, 'polls/detail.html', {'question': question})
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/detail.html', {'question': question}) 

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
# Create your views here.
