from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Pieza, Usuario
from django.core.exceptions import ValidationError

class UsuarioCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Contraseña'}),label="Contraseña")
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Contraseña'}),label="Confirmar Contraseña")
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'telefono','rol','password']
        label = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Email',
            'telefono': 'Telefono',
            'rol': 'Rol',
            'password': 'Contraseña',
            'password_confirm': 'Confirmar Contraseña',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono', 'label':'Teléfono'}),
            'rol': forms.Select(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(),
            'password_confirm': forms.PasswordInput(),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email = email).exists():
            raise ValidationError("Este correo electrónico ya está registrado.")
        return email
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Las contraseñas no coinciden.")
        return cleaned_data
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UsuarioLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)


class PiezaForm(forms.ModelForm):
    class Meta:
        model = Pieza
        fields = ['descripcion','numero_serie','ubicacion', 'cantidad_disponible', 'cantidad_minima','categoria_producto','precio_unitario', 'imagen_pieza']
        exclude = ['fecha_registro']
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
            'numero_serie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de Serie'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ubicación'}),
            'cantidad_disponible': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad Disponible'}),
            'cantidad_minima': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad Mínima'}),
            'categoria_producto':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categoria'}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio Unitario'}),
            'imagen_pieza': forms.ClearableFileInput(attrs={'class': 'form-control', 'onchange': 'previewImage(event, "output_image")'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        cantidad_disponible = cleaned_data.get('cantidad_disponible')
        cantidad_minima = cleaned_data.get('cantidad_minima')

        if cantidad_minima > cantidad_disponible:
            raise forms.ValidationError("La cantidad mínima no puede ser mayor que la cantidad disponible.")
        
        return cleaned_data
    
