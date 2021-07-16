# GESTOR FINANCIERO

**Usuarios administradores (admin, amadeusliz) 
Usuarios normales (eherrera, cdubon)<br>
Contraseña unicah2020**

Un grupo de personas ha decidido invertir parte de su capital para iniciar una pequeña
empresa de tipo financiera. Parte de la inversión se utilizará para el desarrollo de una
aplicación web que les permita gestionar la información de sus clientes y transacciones.

La primera etapa del proyecto contiene los requerimientos más importantes para que la
empresa pueda iniciar sus operaciones. 

Se necesitan sus conocimientos como ingeniero de software para el desarrollo del proyecto,
en el cuál recibirá un pago por sus servicios por un monto de $60,000.00 si éste cumple
con todos los requerimientos solicitados, los cuales se detallan a continuación:

1- Registrar clientes (desde admin): $5,000.00
    -> Nombre, Apellido, Dirección, Fecha de nacimiento, Teléfono y Correo

2- Crear cuenta bancaria a un determinado cliente (desde admin): $5,000.00
    -> Fecha creación, estado (Activa | Inactiva), saldo, propietario de la cuenta (Cliente)

3- Realizar depósito a una cuenta (desarrollar) (solo lo puede hacer el superuser): $10,000.00
4- Reallzar retiro a una cuenta (desarrollar) (solo lo puede hacer el superuser): $10,000.00

5- Realizar transferencia entre cuentas (desarrollar) (lo hace el propio cliente): $10,000.00
    -> El cliente inicia sesión (Su usuario se le crea desde admin)

6- El cliente puede ver su saldo actual y sus transacciones: $10,000.00
    -> Requerirá un modelo que almacene las transacciones (deposito, retiro y transferencia)

Diseño de la interfaz: $10,000.00
    -> Usabilidad
    -> Limpieza

Observaciones
    -> El modelo Cliente debe relacionarse al modelo User de Django a través de OneToOneField permitir Nulo.
        from django.contrib.auth.models import User <- Modelo User de Django
    -> Al momento de iniciar sesión, determinar si es superuser o no y así redirigir a su
       correspondiente página.

