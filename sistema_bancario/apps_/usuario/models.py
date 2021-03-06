from __future__ import unicode_literals
from django.db import models
from django.utils.timezone import now

class Rol(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return '{}'.format(self.nombre)


class Usuario(models.Model):
    cod_usuario = models.AutoField(primary_key=True)
    num_cuenta  = models.BigIntegerField(unique=True)
    full_name   = models.CharField(max_length=100, blank=False, null=False)
    nick_name   = models.CharField(max_length=12, unique=True, blank=False, null=False)
    correo      = models.EmailField(unique=True, blank=False, null=False)
    password    = models.CharField(max_length=8, blank=False, null=False)
    monto       = models.DecimalField(max_digits=6, decimal_places=2, default=0, blank=True, null=False)
    rol         = models.ForeignKey(Rol, null=False, blank=False, on_delete=models.CASCADE)

    def __unicode__(self):
        return '{} ({})'.format(self.nick_name, self.correo)


class Debito(models.Model):
    cuenta = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=6, decimal_places=2, default=0, blank=True, null=False)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField(auto_now_add=True, blank=True)

    def __unicode__(self):
        return '{}'.format(self.cuenta, self.descripcion, self.fecha_reg)


class Transferencia(models.Model):
    cod_transferencia = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
    monto = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    origen_cod_usuario = models.ForeignKey(
        Usuario, related_name="%(class)s_origen", null=False, blank=False, on_delete=models.CASCADE)
    destino_cod_usuario = models.ForeignKey(
        Usuario, related_name="%(class)s_destino", null=False, blank=False, on_delete=models.CASCADE)

    def __unicode__(self):
        return 'Transferencia No.: {} de la cuenta {} a'
        'la cuenta {} con monto {}'.format(self.cod_transferencia,
                                           self.origen_cod_usuario,
                                           self.destino_cod_usuario,
                                           self.monto)


class EstadoCredito(models.Model):
    cod_estado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return '{}'.format(self.nombre)


class Credito(models.Model):
    cod_credito = models.AutoField(primary_key=True)
    monto = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    descripcion = models.TextField(blank=False)
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
    fecha_aprob = models.DateTimeField(blank=True, default=now)
    cod_usuario = models.ForeignKey(
        Usuario, null=False, blank=False, on_delete=models.CASCADE)
    cod_estado = models.ForeignKey(
        EstadoCredito, null=False, blank=False, on_delete=models.CASCADE)

    def __unicode__(self):
        return 'Credito: {}, Monto: {}, Descripcion: {}'.format(
            self.cod_credito, self.monto, self.descripcion)


class Notificacion(models.Model):
    cod_notificacion = models.AutoField(primary_key=True)
    descripcion = models.TextField(blank=False)
    url = models.TextField(blank=True, null=True)
    cod_usuario = models.ForeignKey(
        Usuario, null=False, blank=False, on_delete=models.CASCADE)
    
    def __unicode__(self):
        return '{}'.format(self.descripcion)