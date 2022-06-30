from django import http
import requests
from django.shortcuts import redirect, render

from .models import Questions

def index(request):
    return render(request, 'questions/index.html')

def question(request, question_id):

    if not 'answers' in request.session or question_id == 1:
        request.session['answers'] = []

    

    # Logic for each answer chosen
    if 'answer_one' in request.POST:
        skill = [x for x in request.POST.get('skills').split(',')]
        answer_list = request.session['answers']
        if '&' in skill[0]:
            skills = skill[0].split("&")
            for skill in skills:
                answer_list.append(skill)
        else:
            answer_list.append(skill[0])
        request.session['answers'] = answer_list
        question_id = question_id + 1
        print(request.session['answers'])
        return redirect(f'/question/{question_id}') if question_id < 11 else redirect('/career')

    elif 'answer_two' in request.POST:
        skill = [x for x in request.POST.get('skills').split(',')]
        answer_list = request.session['answers']
        if '&' in skill[1]:
            skills = skill[1].split("&")
            for skill in skills:
                answer_list.append(skill)
        else:
            answer_list.append(skill[1])
        request.session['answers'] = answer_list
        question_id = question_id + 1
        print(request.session['answers'])
        return redirect(f'/question/{question_id}') if question_id < 11 else redirect('/career')

    elif 'answer_three' in request.POST:
        skill = [x for x in request.POST.get('skills').split(',')]
        answer_list = request.session['answers']
        if '&' in skill[2]:
            skills = skill[2].split("&")
            for skill in skills:
                answer_list.append(skill)
        else:
            answer_list.append(skill[2])
        request.session['answers'] = answer_list
        question_id = question_id + 1
        print(request.session['answers'])
        return redirect(f'/question/{question_id}') if question_id < 11 else redirect('/career')

    elif 'answer_four' in request.POST:
        skill = [x for x in request.POST.get('skills').split(',')]
        answer_list = request.session['answers']
        if '&' in skill[3]:
            skills = skill[3].split("&")
            for skill in skills:
                answer_list.append(skill)
        else:
            answer_list.append(skill[3])
        request.session['answers'] = answer_list
        question_id = question_id + 1
        print(request.session['answers'])
        return redirect(f'/question/{question_id}') if question_id < 11 else redirect('/career')

    question = Questions.objects.get(pk=question_id)
    context = {'question' : question}

    return render(request, 'questions/question.html', context)

    

