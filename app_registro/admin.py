from django.contrib import admin
from .models import Cliente, Cuenta, Transaccion

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'correo', 'user')
    list_editable = ('user',) #las tuplas con solo un elemento debe llevar una coma para que entienda que es una tupla

class CuentaAdmin(admin.ModelAdmin):
    list_display = ('id','cliente', 'fecha_creacion', 'estado', 'saldo')
    list_editable = ('estado',) #las tuplas con solo un elemento debe llevar una coma para que entienda que es una tupla


class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('id','cuenta', 'tipo_transaccion', 'monto')
    # list_editable = ('estado',) #las tuplas con solo un elemento debe llevar una coma para que entienda que es una tupla


admin.site.register(Cliente, ClienteAdmin)

admin.site.register(Cuenta, CuentaAdmin)

admin.site.register(Transaccion, TransaccionAdmin)

# admin.site.register(Cliente)

# admin.site.register(Cuenta)
