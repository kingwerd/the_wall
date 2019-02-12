from django.shortcuts import render, redirect
from django.contrib import messages

import bcrypt

from .models import User

def index(request):
    return render(request, 'login_register/login-register.html')

def register_user(request):
    if request.method == "POST":
        data = request.POST
        errors = User.objects.registration_validator(data)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            password = data['password'].encode()
            password = bcrypt.hashpw(password, bcrypt.gensalt()).decode()
            print(password)
            user = User.objects.create(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], password=password)
            user.save()
            request.session['user_id'] = user.id
            context = {
                'user': user
            }
            return redirect('/wall/')

def login_user(request):
    if request.method == "POST":
        data = request.POST
        errors = User.objects.login_validator(data)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            user = User.objects.get(email=data['login_email'])
            request.session['user_id'] = user.id
            return redirect('/wall/')

def logout(request):
    print('logout called')
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('/')