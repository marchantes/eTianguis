# -*- encoding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from applications.models import Producto

class IndexView(TemplateView):
    template_name = "applications/index.html"
"""
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
    return render(request, 'applications/login.html', context)

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
"""

class ProductCreate(CreateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'imagen', 'precio']
    success_url = "/applications/"

class UserCreate(CreateView):
    model = User
    template_name = "applications/user_form.html"
    fields = ['first_name', 'last_name', 'email', 'username', 'password']
    success_url = "/applications/"