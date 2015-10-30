from django.forms import ModelForm
from applications.models import Usuario, Producto


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre',
                  'appellido',
                  'mail',
                  'username',
                  'password'
        ]

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre',
                  'descripcion',
                  'imagen',
                  'precio' 
        ]