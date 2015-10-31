from django.forms import ModelForm
from applications.models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre',
                  'descripcion',
                  'imagen',
                  'precio' 
        ]