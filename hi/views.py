from django.shortcuts import render, redirect
from .models import User
from django.db import IntegrityError

def user_list(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})

def add_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        age = request.POST['age']  
        try:
            user = User(email=email, name=name, age=age)  
            user.save()
            return redirect('index')
        except IntegrityError:
            return render(request, 'index.html', {
                'users': User.objects.all(),
                'error': 'This email is already in use.'
            })
    return redirect('/')
