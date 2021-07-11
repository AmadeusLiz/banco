from django.urls import path
from . import views

app_name = 'registro'

urlpatterns = [
    path('', views.index, name="index"),
    path('clientes/', views.clientes, name="clientes"),
    path('clientes/deposito_retiro/<int:id>/<str:accion>/', views.deposito_retiro, name="deposito_retiro"),
    path('clientes/depositar/<int:id>/', views.depositar, name="depositar"),
    path('clientes/retirar/<int:id>/', views.retirar, name="retirar"),
    path('transacciones/', views.transacciones, name="transacciones"),
    path('transferencias/', views.transferencias, name="transferencias"),
    # path('', , name=""),
] 