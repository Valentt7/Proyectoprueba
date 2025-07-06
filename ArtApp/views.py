from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SolicitudComisionForm
from .models import SolicitudComision

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
                return redirect('form')  # Redirigir para evitar reenvío
            except Exception as e:
                messages.error(request, f'Error al guardar la solicitud: {str(e)}')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = SolicitudComisionForm()
    
    return render(request, 'form.html', {'form': form})

def listar_solicitudes(request):
    solicitudes = SolicitudComision.objects.all().order_by('-fecha_creacion')
    return render(request, 'admin.html', {'solicitudes': solicitudes})

# Create your views here.
