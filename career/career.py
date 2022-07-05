import random
from re import L

def job(specialSkills, skills, name):

    specialSkills = specialSkills.split(',')
    skills = skills.split(',')

    return {
        'name' : name,
        'strength' : random.randint(1, int(specialSkills[0])),
        'perception' : random.randint(1, int(specialSkills[1])),
        'endurance' : random.randint(1, int(specialSkills[2])),
        'charisma' : random.randint(1, int(specialSkills[3])),
        'intelligence' : random.randint(1, int(specialSkills[4])),
        'agility' : random.randint(1, int(specialSkills[5])),
        'luck' : random.randint(1, int(specialSkills[6])),
        'barter' : random.randint(1, int(skills[0])),
        'big_guns' : random.randint(1, int(skills[1])),
        'energy_weapons' : random.randint(1, int(skills[2])),
        'explosives' : random.randint(1, int(skills[3])),
        'lock_pick' : random.randint(1, int(skills[4])),
        'medicine' : random.randint(1, int(skills[5])),
        'melee_weapons' : random.randint(1, int(skills[6])),
        'repair' : random.randint(1, int(skills[7])),
        'science' : random.randint(1, int(skills[8])),
        'small_guns' : random.randint(1, int(skills[9])),
        'sneak' : random.randint(1, int(skills[10])),
        'speech' : random.randint(1, int(skills[11])),
        'unarmed' : random.randint(1, int(skills[12]))
    }




