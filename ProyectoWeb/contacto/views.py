from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.conf import settings

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
            #enviamos el correo con la informacion del formulario
            
            email = EmailMessage(
                'Mensaje de contacto desde Rapid',
                'el usario {} ha enviado el siguiente mensaje: {} y su correo electronico es {}'.format(nombre,mensaje,email),
                '',
                [settings.EMAIL_HOST_USER],
                reply_to=[email],
            )
            
            try:
                email.send()
                return redirect('/contacto/?valid')
            except:
                pass
               # return redirect('/contacto/?invalid')

    return render (request , "contacto/contacto.html", {'miFormulario':formulario_contacto})


