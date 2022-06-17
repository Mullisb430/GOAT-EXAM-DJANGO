from django.views.generic import TemplateView
from django.shortcuts import render

class StartScreen(TemplateView):
    http_method_names = ["get"]
    template_name = "questions/start.html"
