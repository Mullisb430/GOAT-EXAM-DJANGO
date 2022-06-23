from django.views.generic import TemplateView
from django.shortcuts import render

from .models import Questions

class StartScreen(TemplateView):
    http_method_names = ["get"]
    template_name = "questions/start.html"

class QuestionScreen(TemplateView):
    http_method_names = ["get"]
    template_name = "questions/question.html"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        questions = Questions.objects.all()

        count = 0
        for question in questions:
            context[f'question{count}'] = questions
        return context
