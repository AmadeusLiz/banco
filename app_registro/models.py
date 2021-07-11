from django.db import models
from django.db.models.enums import Choices
from datetime import datetime
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator #https://www.it-swarm-es.com/es/python/permitir-solo-numeros-decimales-positivos/1069591008/

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.TextField()
    fecha_nac = models.DateField()
    telefono = models.CharField(max_length=20, null=True, blank=True)
    correo = models.EmailField()
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    ) 

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Cuenta(models.Model):
    ESTADOS = (('0', 'INACTIVA'),('1', 'ACTIVA'))
    fecha_creacion = models.DateTimeField(auto_now_add=True) #agregar fechas de ese momento automaticamente
    estado = models.CharField(max_length=1, choices=ESTADOS, default='1')
    saldo = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0)])
    cliente = models.OneToOneField(
        Cliente,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    ) #propietario de la cuenta

    def __str__(self):
        return f'{self.cliente}'

class Transaccion(models.Model):
    TRANSACCIONES = (
        ('1', 'Depósito'), #BD, INTERFAZ GRAFICA
        ('2', 'Retiro'), 
        ('3', 'Transferencia'), 
    )
        
    tipo_transaccion = models.CharField(max_length=1, choices=TRANSACCIONES, default='1')
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0)])

    def __str__(self):
        return f'{self.cuenta} | {self.tipo_transaccion} '