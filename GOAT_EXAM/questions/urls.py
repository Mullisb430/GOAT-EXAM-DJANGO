from django.urls import path
from . import views

app_name = "questions"

urlpatterns = [
    path('', views.StartScreen.as_view(), name='Start'),
    path('Question/', views.QuestionScreen.as_view(), name='Question')
]