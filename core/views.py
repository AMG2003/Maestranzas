from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django import forms
from .forms import UsuarioCreationForm, UsuarioLoginForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import Pieza, Usuario
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
@login_required
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, "core/lista_usuarios.html", {'usuarios': usuarios})
@login_required
def update_users(request, id):
    usuario = get_object_or_404(Usuario,id = id)
    roles = Usuario.ROL_CHOICES
    contexto = {'datos':usuario,'roles':roles}
    return render(request,"core/modificar_usuarios.html",contexto)
@login_required
def datos_user(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        usuario = get_object_or_404(Usuario,id = id)
        nombre_u = request.POST.get("nombre")
        apellido_u = request.POST.get("apellido")
        email_u = request.POST.get("email")
        telefono_u = request.POST.get("telefono")
        rol_u = request.POST.get("rol")
        foto_u = request.FILES.get("foto", None)
        
        usuario.nombre = nombre_u
        usuario.apellido = apellido_u
        usuario.email = email_u
        usuario.telefono = telefono_u
        usuario.rol = rol_u

        if rol_u == 'Administrador del Sistema':
            usuario.is_superuser = True
            usuario.is_staff = True
        else:
            usuario.is_superuser = False
            usuario.is_staff = False

        if foto_u:
            usuario.imagen_perfil = foto_u

        usuario.save()
        messages.success(request,'Los cambios se han guardado correctamente.')

        if request.user == usuario and not usuario.is_superuser:
            logout(request)
            return redirect('login')
    return redirect("lista_usuarios")
@login_required
def eliminar_usuario(request,id):
    try:
        usuario = get_object_or_404(Usuario,id = id)
        usuario_nombre = usuario.nombre
        usuario.delete()
        messages.success(request,f'El usuario "{usuario.nombre}" ha sido eliminado correctamente.')
    except Exception as e:
        messages.error(request, f'No se pudo eliminar el usuario. Error: {str(e)}')

    return redirect(to="lista_usuarios")

def registro_usuario(request):
    if request.method == "POST":
        formulario = UsuarioCreationForm(request.POST)
        if formulario.is_valid():
            user = formulario.save(commit=False)
            user.set_password(formulario.cleaned_data['password'])
            if user.rol == 'Administrador del Sistema':
                user.is_superuser = True
                user.is_staff = True
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
@login_required
def modificar_pieza(request, pieza_id):
    pieza = get_object_or_404(Pieza, id=pieza_id)
    if request.method == "POST":
        form = PiezaForm(request.POST, request.FILES, instance=pieza)
        if form.is_valid():
            form.save()
            messages.success(request,'Los cambios se han guardado correctamente.')
            return redirect('lista_piezas')
    else:
        form = PiezaForm(instance=pieza)
    return render(request, 'core/modificar_pieza.html', {'form': form})
@login_required
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


    
