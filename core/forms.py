from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Pieza

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',"first_name","last_name","email","password1","password2"]


class PiezaForm(forms.ModelForm):
    class Meta:
        model = Pieza
        fields = ['descripcion','numero_serie','ubicacion', 'cantidad_disponible', 'cantidad_minima','precio_unitario']
        exclude = ['fecha_registro']

    def clean(self):
        cleaned_data = super().clean()
        cantidad_disponible = cleaned_data.get('cantidad_disponible')
        cantidad_minima = cleaned_data.get('cantidad_minima')

        if cantidad_minima > cantidad_disponible:
            raise forms.ValidationError("La cantidad mínima no puede ser mayor que la cantidad disponible.")
        
        return cleaned_data