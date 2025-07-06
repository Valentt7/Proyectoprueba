from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def form(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        tipo = request.POST.get('tipo')
        descripcion = request.POST.get('descripcion')
        referencias = request.POST.get('referencias')

        # Aquí podrías guardar los datos en la base de datos si es necesario

        return render(request, 'form.html', {'nombre': nombre, 'email': email, 'tipo': tipo, 'descripcion': descripcion, 'referencias': referencias})


# Create your views here.
