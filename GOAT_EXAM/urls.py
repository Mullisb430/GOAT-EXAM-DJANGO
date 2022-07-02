"""GOAT_EXAM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from questions import urls as questions_urls
from career import urls as career_urls
from career import views as career_views
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(questions_urls, namespace='questions') ),
    path('career', career_views.career, name='career' ),
    path('loading', career_views.loading, name='loading')
]
