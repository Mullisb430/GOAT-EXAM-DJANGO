from django.urls import path
from . import views
from career import views as career_views

app_name = "questions"

urlpatterns = [
    path('', views.index),
    path('question/<int:question_id>/', views.question),
    path('career', career_views.career)
]