import random

def generate():
    names = ['Крош', 'Халк', 'Человек Паук', 'КарКарыч', 'Лосяш', 'Железный Человек']
    return names[random.randint(0, 5)]
