from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SolicitudComisionForm
from .models import SolicitudComision
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

def index(request):
    return render(request,'index.html')

def form(request):
    if request.method == 'POST':
        form = SolicitudComisionForm(request.POST)
        if form.is_valid():
            try:
                # Guardar en la base de datos MySQL
                solicitud = form.save()
                messages.success(request, f'¡Solicitud enviada exitosamente! ID: {solicitud.id}')
                return redirect('form') 
            except Exception as e:
                messages.error(request, f'Error al guardar la solicitud: {str(e)}')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = SolicitudComisionForm()
    
    return render(request, 'form.html', {'form': form})

@login_required
def administracion(request):
    solicitudes = SolicitudComision.objects.all().order_by('-fecha_creacion')
    return render(request, 'admin.html', {'solicitudes': solicitudes})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lista_solicitudes')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect('login')

def actualizar_estado(request, solicitud_id):
    if request.method == 'POST':
        try:
            solicitud = SolicitudComision.objects.get(id=solicitud_id)
            nuevo_estado = request.POST.get('estado')
            solicitud.estado = nuevo_estado
            solicitud.save()
            messages.success(request, 'Estado actualizado correctamente')
        except SolicitudComision.DoesNotExist:
            messages.error(request, 'Solicitud no encontrada')
    return redirect('administracion')
# Create your views here.
