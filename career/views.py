from django.shortcuts import render
import random

def career(request):
    career = careerAlgo(request)

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

    career = random.choice(POTENTIAL_CAREERS)

    if career == 'Vault Chaplain':
        pass

    

