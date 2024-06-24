from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django import forms
from .forms import UsuarioCreationForm, UsuarioLoginForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import Pieza
from .forms import PiezaForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from carro.carro import Carro
# Create your views here.
def home(request):
    carro = Carro(request)
    return render(request, "core/home.html")
def base(request):
    return render(request, "core/base.html")

def logout_usuario(request):
    logout(request)
    return redirect('home')

def registro_usuario(request):
    if request.method == "POST":
        formulario = UsuarioCreationForm(request.POST)
        if formulario.is_valid():
            user = formulario.save(commit=False)
            user.set_password(formulario.cleaned_data['password'])
            user.save()
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        else:
            messages.error(request,'Corrige los errores a continuación.')
            return render(request, "registration/registro.html", {'formulario': formulario})
    else:
        formulario = UsuarioCreationForm()
    return render(request, "registration/registro.html", {'formulario': formulario})

def login_usuario(request):
    if request.method == 'POST':
        formulario = UsuarioLoginForm(request, data = request.POST)
        if formulario.is_valid():
            email = formulario.cleaned_data.get('username')
            contraseña = formulario.cleaned_data.get('password')
            user = authenticate(request, email=email, password=contraseña)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        formulario = UsuarioLoginForm()
    return render(request, 'login.html', {'formulario': formulario})
    
@login_required
def perfil(request):
    return render(request, "core/perfil.html")

@login_required
def registrar_pieza(request):
    if request.method == 'POST':
        form = PiezaForm(request.POST,request.FILES)
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

def carrito(request):
    return render(request, 'core/carrito.html')

def calculate_shopping_cart_total(request):
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session.get("carro", {}).items():
            total += float(value.get("precio_unitario",0))
    return total


    
