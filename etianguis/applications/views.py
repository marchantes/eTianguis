from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.edit import CreateView, FormView
from applications.models import Producto, Transaccion
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User


class IndexView(TemplateView):
    template_name = "applications/index.html"


class ProductCreate(SuccessMessageMixin, CreateView):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCreate, self).dispatch(request, *args, **kwargs)

    model = Producto
    fields = ['nombre', 'descripcion', 'imagen', 'precio']
    success_url = reverse_lazy('applications:product')
    success_message = "Your product was created successfully"

    def form_valid(self, form):
        user = self.request.user
        form.instance.id_usuario = user
        return super(ProductCreate, self).form_valid(form)


class ProductList(ListView):
    model = Producto
    template_name = "applications/products.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.request.user.id)
        self.queryset = Producto.objects.exclude(id_usuario=user)
        return super(ProductList, self).dispatch(request, *args, **kwargs)


class ProductDetail(SuccessMessageMixin, DetailView):
    model = Producto

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ProductDetail, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        return context


class ProductPurchase(CreateView):
    model = Transaccion
    fields = ['cantidad']
    success_url = reverse_lazy('applications:product')
    template_name = "applications/product_purchase.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        # user = self.request.user
        print(request)
        return super(ProductPurchase, self).dispatch(request, *args, **kwargs)


class UserCreate(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    template_name = "applications/user_form.html"
    success_url = reverse_lazy('applications:index')
    success_message = "User was created successfully"


class UserLogin(SuccessMessageMixin, FormView):
    form_class = AuthenticationForm
    template_name = "applications/login.html"
    success_url = reverse_lazy('applications:product')
    success_message = "Welcome back %(username)s!"

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
