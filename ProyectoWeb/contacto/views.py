from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.contrib import messages

# Create your views here.
def contacto(request):
    formulario_contacto = FormularioContacto()
    
    if request.method == "POST":
        formulario_contacto = FormularioContacto(data= request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            mensaje = request.POST.get('mensaje')
            messages.success(request, 'Mensaje enviado correctamente')

            return redirect('contacto/contacto/?valid')


    return render (request , "contacto/contacto.html", {'miFormulario':formulario_contacto})


