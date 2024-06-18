from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import logout
from django import forms
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import Pieza
from .forms import PiezaForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
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
    query = request.GET.get('q')
    if query:
        piezas = Pieza.objects.filter(descripcion__icontains=query)
    else:
        piezas = Pieza.objects.all()
    paginator = Paginator(piezas, 10)
    page_number = request.GET.get('page')
    piezas = paginator.get_page(page_number)
    return render(request, 'core/lista_piezas.html', {'piezas': piezas, 'query': query})

def piezas(request):
    piezas = Pieza.objects.all()
    data = {"pieza": piezas}
    return render(request, "core/piezas.html", data)

def eliminar_pieza(request,id):
    pieza = get_object_or_404(Pieza,id = id)
    pieza.delete()
    return redirect(to="lista_piezas")

def detalle_pieza(request, pieza_id):
    pieza = get_object_or_404(Pieza, id=pieza_id)
    return render(request, 'core/detalle_pieza.html', {'pieza': pieza})

    
