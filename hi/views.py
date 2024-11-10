# gold/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ActivityLog
import random

def gold(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activity_log' not in request.session:
        request.session['activity_log'] = []

    context = {
        'gold': request.session['gold'],
        'activity_log': request.session['activity_log']
    }
    return render(request, 'index.html', context)

def process_money(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        gold_change = 0
        action = ''

        if location == 'farm':
            gold_change = random.randint(10, 20)
            action = f"Earned {gold_change} gold from the farm!"
        elif location == 'cave':
            gold_change = random.randint(5, 10)
            action = f"Earned {gold_change} gold from the cave!"
        elif location == 'house':
            gold_change = random.randint(2, 5)
            action = f"Earned {gold_change} gold from the house!"
        elif location == 'quest':
            gold_change = random.randint(-50, 50)
            if gold_change >= 0:
                action = f"Completed a quest and earned {gold_change} gold!"
            else:
                action = f"Failed a quest and lost {abs(gold_change)} gold!"

        request.session['gold'] += gold_change
        request.session['activity_log'].insert(0, {'action': action, 'amount': gold_change})

        activity = ActivityLog(action=action, amount=gold_change)
        activity

        return redirect('/')
    else:
        return HttpResponse("Invalid request.")
