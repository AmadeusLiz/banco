from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse

def index(request):
    if request.user.is_authenticated:
        # return redirect(reverse('registro:index'))
        return render(request, 'registro/clientes.html')
    return render(request, 'seguridad/index.html')

def log_in(request):
    if request.method == "POST":
        username = request.POST.get('usuario')
        password = request.POST.get('passw')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect(reverse('registro:clientes'))
            else:
                return redirect(reverse('registro:index'))

        else:
            messages.add_message(request, messages.ERROR, 'El usuario/contraseña inválidos o la cuenta está desactivada')
            return redirect('/')

    else:
        return redirect('/')

def log_out(request):
    logout(request)
    return redirect('/')
