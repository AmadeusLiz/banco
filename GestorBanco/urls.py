"""GestorBanco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app_seguridad import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('inicio/', include('app_registro.urls')),
    # path('registro/', include('app_registro.urls')),
    path('login/', views.log_in, name="login_view"),
    path('logout/', views.log_out, name="logout_view"),


    # path('', views.index, name="index"),
    # path('clientes/', views.clientes, name="clientes"),
    # path('clientes/deposito_retiro/<int:id>/<str:accion>/', views.deposito_retiro, name="deposito_retiro"),
    # path('clientes/depositar/<int:id>/', views.depositar, name="depositar"),
    # path('clientes/retirar/<int:id>/', views.retirar, name="retirar"),
    # path('transacciones/', views.transacciones, name="transacciones"),


]
