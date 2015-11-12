from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.edit import CreateView, DeleteView, FormView
from applications.models import Producto, Transaccion
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView
from django.contrib.messages.views import SuccessMessageMixin
# from django.contrib.auth.models import User


class IndexView(TemplateView):
    template_name = "applications/index.html"


class ProductCreate(SuccessMessageMixin, CreateView):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCreate, self).dispatch(request, *args, **kwargs)

    model = Producto
    fields = ['nombre', 'descripcion', 'imagen', 'precio']
    success_url = reverse_lazy('applications:products')
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
        user = self.request.user
        self.queryset = Producto.objects.exclude(
            id_usuario=user).exclude(cantidad=0)
        return super(ProductList, self).dispatch(request, *args, **kwargs)


class ProductDetail(SuccessMessageMixin, DetailView):
    model = Producto

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ProductDetail, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        return context


class ProductDelete(SuccessMessageMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy('applications:products')
    success_message = "Product deleted successfully."
    template_name = "applications/confirm_delete.html"


class ProductPurchase(SuccessMessageMixin, CreateView):
    model = Transaccion
    fields = ['cantidad']
    success_url = reverse_lazy('applications:products')
    success_message = "Product purchased successfully."
    template_name = "applications/product_purchase.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        producto = Producto.objects.get(pk=self.kwargs['pk'])
        producto.cantidad -= 1
        return super(ProductPurchase, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = self.request.user
        actual_primary_key = self.kwargs['pk']
        producto = Producto.objects.get(pk=actual_primary_key)
        form.instance.id_usuario = user
        form.instance.id_producto = producto
        producto.cantidad -= 1
        producto.save()
        self.Transaccion = form.save()
        return super(ProductPurchase, self).form_valid(form)


class UserCreate(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    template_name = "applications/user_form.html"
    success_url = reverse_lazy('applications:index')
    success_message = "User was created successfully"


class UserLogin(SuccessMessageMixin, FormView):
    form_class = AuthenticationForm
    template_name = "applications/login.html"
    success_url = reverse_lazy('applications:products')
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


class UserProducts(ListView):
    model = Producto
    template_name = "applications/user_products.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        self.queryset = Producto.objects.filter(id_usuario=user)
        return super(UserProducts, self).dispatch(request, *args, **kwargs)


class UserPurchases(ListView):
    model = Transaccion
    template_name = "applications/user_purchases.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        self.queryset = Transaccion.objects.filter(id_usuario=user)
        return super(UserPurchases, self).dispatch(request, *args, **kwargs)
