from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm #creacion de formulario
from django.contrib.auth.models import User #registro de usuarios
from django.http import HttpResponse #enviar mensaje por html
# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    
    if request.method == 'GET': #envia el formulario
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else: #obtiene los datos - POST
        if request.POST['password1'] == request.POST['password2']:
            try:
                #register user
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1']) #crea el usuario
                user.save()
                return HttpResponse('usuario creado correctamente') 
            except:
                return HttpResponse('El usuario ya existe')
    
        return HttpResponse('Las contrasenias no concuerdan')