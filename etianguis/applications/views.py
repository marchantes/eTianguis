from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.views.generic import TemplateView, ListView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.edit import CreateView, FormView
from applications.models import Producto
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone
from django.views.generic.base import RedirectView


class IndexView(TemplateView):
    template_name = "applications/index.html"


class ProductCreate(CreateView):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCreate, self).dispatch(request, *args, **kwargs)

    model = Producto
    fields = ['nombre', 'descripcion', 'imagen', 'precio']
    success_url = reverse_lazy('applications:product')


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
    form_class = UserCreationForm
    template_name = "applications/user_form.html"
    success_url = reverse_lazy('applications:index')


class UserLogin(FormView):
    form_class = AuthenticationForm
    template_name = "applications/login.html"
    success_url = reverse_lazy('applications:product')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(self.get_success_url())
        else:
            return super(UserLogin, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(UserLogin, self).form_valid(form)


class UserLogout(RedirectView):
    pattern_name = 'applications:index'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(UserLogout, self).get(request, *args, **kwargs)
