# Generated by Django 3.2.3 on 2021-07-07 22:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_registro', '0004_alter_cuenta_saldo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_transaccion', models.CharField(choices=[('1', 'Depósito'), ('2', 'Retiro'), ('3', 'Transferencia')], default='1', max_length=1)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_registro.cuenta')),
            ],
        ),
    ]
