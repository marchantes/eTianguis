# -*- encoding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from applications.models import Producto
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone

class IndexView(TemplateView):
    template_name = "applications/index.html"

class ProductCreate(CreateView):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCreate, self).dispatch(request, *args, **kwargs)
    
    model = Producto
    fields = ['nombre', 'descripcion', 'imagen', 'precio']
    success_url = reverse_lazy("product")

class ProductList(ListView):
    model = Producto
    template_name = "applications/products.html"
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ProductList, self).dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class UserCreate(CreateView):
    model = User
    template_name = "applications/user_form.html"
    fields = ['first_name', 'last_name', 'email', 'username', 'password']
    success_url = reverse_lazy("index")

class UserLogin(FormView):
    form_class = AuthenticationForm
    template_name = "applications/login.html"
    success_url = reverse_lazy("product")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(self.get_success_url())
        else:
            return super(UserLogin, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(UserLogin, self).form_valid(form)
