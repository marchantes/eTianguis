# -*- encoding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def index(request):
    template = loader.get_template('applications/index.html')
    return HttpResponse(template.render(context))

def user_login(request):
    login_form = AuthenticationForm()
    context = {'login_form': login_form, }
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                context['message'] = "Usuario existente y activo"
                login(request, user)
                return redirect('/')
            else:
                context['message'] = "El usuario existe pero no está activo"
        else:
            context['message'] = "No existe el usuario"
    return render(request, 'applications/index.html', context)

def user_signup(request):
    signup_form = UserCreationForm()
    context = {'signup_form': signup_form,}
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        if (username and password and email and first_name and last_name):
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            userprofile = UserProfile(user=user)
            userprofile.save()
            return redirect('/')
    return render(request, 'applications/signup.html', context)
