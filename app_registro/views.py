from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from decimal import Decimal
from .models import Cliente, Cuenta, Transaccion
from django.db import transaction #https://docs.djangoproject.com/en/3.2/topics/db/transactions/
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

@login_required()
def index(request):
    return render(request, 'registro/index.html')

@login_required()
@user_passes_test(lambda u: u.is_superuser) #https://stackoverflow.com/questions/15998140/how-to-limit-a-view-to-superuser-only/47689629
def clientes(request):
    activo = 'clientes'

    q = request.GET.get('q')

    if q:
        data = Cliente.objects.filter(nombre__startswith=q).order_by('nombre') #buscar por nombre
    else:
        data = Cliente.objects.all().order_by('nombre') #'-nombre' para ordenar descendednte nos regresa todos los registros que tiene participante

    ctx = {
        'clientes': data,
        'q': q,
        'activo': activo
    }

    return render(request, 'registro/clientes.html', ctx) #recibe minimo 2 parametros

@login_required()
def deposito_retiro(request, id, accion):
    data = get_object_or_404(Cuenta, cliente=id) #datos de la cuenta, se debe hacer por el id del cliente, no con pk porque son diferentes

    activo = 'superuser'

    if accion!="depositar" and accion!="retirar":
        accion = "invalid"        

    ctx = {
        'data': data,
        'activo': activo,
        'accion': accion
    }

    return render(request, 'registro/deposito_retiro.html', ctx)

@login_required()
def depositar(request, id):
    if request.method == 'POST':
        try:
            with transaction.atomic():
                cta = get_object_or_404(Cuenta, pk=id) #el id que se recibe es el de la cuenta

                #Realizar el deposito
                monto = Decimal(request.POST.get('monto'))
                cta.saldo += monto
                cta.save()

                #Añadir la transaccion 
                Transaccion.objects.create(tipo_transaccion='1', cuenta=cta, monto=monto)

                activo = 'superuser'

                ctx = {
                    'data': cta,
                    'activo': activo,
                    'accion': 'depositar'
                }
                messages.add_message(request, messages.INFO,  f'Depósito realizado con éxito')
                return render(request, 'registro/deposito_retiro.html',ctx)
        except Exception as e:
            print(e)
            messages.add_message(request, messages.ERROR,  f'<strong>OCURRIÓ UN ERROR AL HACER EL DEPÓSITO</strong>')
        return render(request, 'registro/clientes.html')
    # return redirect(reverse('deposito_retiro'))

@login_required()
def retirar(request, id):
    if request.method == 'POST':
        try:
            with transaction.atomic():
                cta = get_object_or_404(Cuenta, pk=id) #el id que se recibe es el de la cuenta

                monto = Decimal(request.POST.get('monto'))
                if cta.saldo >= monto: #validar para no sacar mas de la cuenta
                    #Realizar el retiro
                    cta.saldo -= monto
                    cta.save()

                    #Añadir la transaccion 
                    Transaccion.objects.create(tipo_transaccion='2', cuenta=cta, monto=monto)

                    messages.add_message(request, messages.INFO,  f'Retiro realizado con éxito')
                else:
                    messages.add_message(request, messages.ERROR,  f'<strong>FONDOS INSUFICIENTES</strong>')

                activo = 'superuser'

                ctx = {
                    'data': cta,
                    'activo': activo,
                    'accion': 'retirar'
                }

        except Exception as e:
            print(e)
            messages.add_message(request, messages.ERROR,  f'<strong>OCURRIÓ UN ERROR AL HACER EL RETIRO</strong>')
            
        return render(request, 'registro/deposito_retiro.html',ctx)

@login_required()
def transacciones(request):
    activo = 'transacciones'
    transacciones = Transaccion.objects.all().order_by('cuenta')
    transacciones = transacciones.filter(cuenta=request.user.cliente.cuenta.id)

    ctx = {
        'transacciones': transacciones,
        'activo': activo,
        'cuenta': request.user.cliente.cuenta.saldo
    }

    return render(request, 'registro/transacciones.html', ctx)

@login_required()
def transferencias(request):
    if request.method == 'POST':
        try:
            #Obtener datos del formulario
            monto = Decimal(request.POST.get('monto'))

            #Obtener las cuentas
            ctaDestino = get_object_or_404(Cuenta, pk=request.POST.get('cuenta')) #el id que se recibe es el de la cuenta
            ctaOrigen = get_object_or_404(Cuenta, pk=request.user.cliente.cuenta.id)

            if ctaDestino.id == ctaOrigen.id:
                messages.add_message(request, messages.ERROR,  f'<strong>POR FAVOR, INGRESE UNA CUENTA DIFERENTE A LA SUYA</strong>')
            else:
                with transaction.atomic():
                    if ctaOrigen.saldo >= monto: #validar para no sacar mas de la cuenta
                        #Añadir la transaccion 
                        Transaccion.objects.create(tipo_transaccion='3', cuenta=ctaOrigen, monto=monto)
                        Transaccion.objects.create(tipo_transaccion='3', cuenta=ctaDestino, monto=monto)

                        #Realizar retiro a cuenta del que transfirio 
                        ctaOrigen.saldo -= monto
                        ctaOrigen.save() 

                        #Realizar el deposito a cuenta
                        ctaDestino.saldo += monto
                        ctaDestino.save()

                        messages.add_message(request, messages.INFO,  f'Transferencia realizada con éxito')
                    else:
                        messages.add_message(request, messages.ERROR,  f'<strong>FONDOS INSUFICIENTES</strong>')
        except Exception as e:
            print(e)
            messages.add_message(request, messages.ERROR,  f'<strong>OCURRIÓ UN ERROR AL HACER LA TRANSFERENCIA</strong>')

    ctaOrigen = get_object_or_404(Cuenta, pk=request.user.cliente.cuenta.id) #para actualizar saldo traer de vuelta el objeto
    
    ctx = {
        'activo': 'transferencias',
        'cuenta': ctaOrigen.saldo
    }
    return render(request, 'registro/transferencia.html', ctx)