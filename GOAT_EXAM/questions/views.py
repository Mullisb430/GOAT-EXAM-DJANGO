import requests
from django.shortcuts import render

from .models import Questions

def index(request):
    questions = Questions.objects.get(pk=1)

    context = {'question' : question}
    return render(request, 'questions/index.html', context)

def question(request, question_id):
    question = Questions.objects.get(pk=question_id)
    context = {'question' : question}
    return render(request, 'questions/question.html', context)


    # def dispatch(self, request, *args, **kwargs):
    #     self.request = request
    #     return super().dispatch(request, *args, **kwargs)

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['questions'] = Questions.objects.all()
        
    #     return context

