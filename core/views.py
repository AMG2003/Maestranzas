from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django import forms
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import Pieza
from .forms import PiezaForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, "core/home.html")
def base(request):
    return render(request, "core/base.html")

def exit(request):
    logout(request)
    return redirect('home')

def registro(request):
    data = {"form": CustomUserCreationForm()}

    if request.method == "POST":
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(
                username=formulario.cleaned_data["username"],
                password=formulario.cleaned_data["password1"],
            )
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario

    return render(request, "registration/registro.html", data)
@login_required
def perfil(request):
    return render(request, "core/perfil.html")
@login_required
def registrar_pieza(request):
    if request.method == 'POST':
        form = PiezaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_piezas')
        else:
            return render(request, 'core/registrar_pieza.html', {'form': form})
    else:
        form = PiezaForm()
    return render(request, 'core/registrar_pieza.html', {'form': form})
@login_required
def lista_piezas(request):
    piezas = Pieza.objects.all()
    return render(request, 'core/lista_piezas.html', {'piezas': piezas})