from pickle import NONE
from django.shortcuts import redirect, render
import random
from .models import Career
from .career import job


def career(request):
    if not 'answers' in request.session:
        return redirect('/')

    if not 'job' in request.session:
        request.session['job'] = careerAlgo(request)
    
    career = request.session['job']

    context = {
        'career' : career
    }

    return render(request, 'career/career.html', context)

def loading(request):
    return render(request, 'career/loading.html')



def careerAlgo(request):
    POTENTIAL_CAREERS = ['Vault Chaplain', 'Laundry Cannon Operator', 'Pedicurist', 'Waste Management Specialist', 'Vault Loyalty Inspector', 'Clinical Test Subject', 'Fry Cook', 'Jukebox Technician', 'Pip-Boy Programmer', 'Tattoo Artist', 'Shift Supervisor', 'Marriage Counselor', 'Little League Coach', 'Masseuse']

    if not 'barter' in request.session['answers']:
        POTENTIAL_CAREERS.remove('Vault Chaplain')

    elif not 'big' in request.session['answers']:
        POTENTIAL_CAREERS.remove('Laundry Cannon Operator')

    elif not 'energy' in request.session['answers']:
        POTENTIAL_CAREERS.remove('Pedicurist')

    elif not 'explosives' in request.session['answers']:
        POTENTIAL_CAREERS.remove('Waste Management Specialist')

    elif not 'lockpick' in request.session['answers']:
        POTENTIAL_CAREERS.remove('Vault Loyalty Inspector')

    elif not 'medicine' in request.session['answers']:
        POTENTIAL_CAREERS.remove('Clinical Test Subject')

    elif not 'melee' in request.session['answers']:
        POTENTIAL_CAREERS.remove('Fry Cook')

    elif not 'repair' in request.session['answers']:
        POTENTIAL_CAREERS.remove('Jukebox Technician')

    elif not 'science' in request.session['answers']:
        POTENTIAL_CAREERS.remove('Pip-Boy Programmer')

    elif not 'small' in request.session['answers']:
        POTENTIAL_CAREERS.remove('Tattoo Artist')

    elif not 'sneak' in request.session['answers']:
        POTENTIAL_CAREERS.remove('Shift Supervisor')

    elif not 'speech' in request.session['answers']:
        POTENTIAL_CAREERS.remove('Marriage Counselor')

    elif not 'unarmed' in request.session['answers']:
        POTENTIAL_CAREERS.remove('Little League Coach')

    role = random.choice(POTENTIAL_CAREERS)
    role = Career.objects.get(name=role)
    return job(role.special, role.skills, role.name)

     

    

    
    

    

