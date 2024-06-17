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
        fields = ['descripcion','numero_serie','ubicacion', 'cantidad_disponible', 'cantidad_minima']
        exclude = ['fecha_registro']
