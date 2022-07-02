from django.urls import path
from . import views

app_name = "career"

urlpatterns = [
    path('career', views.career, name='career'),
    path('loading', views.loading, name='loading')
]