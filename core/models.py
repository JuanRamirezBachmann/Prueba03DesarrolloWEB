from django.db import models

# Create your models here.
class Clientes(models.Model):
    idMascota = models.IntegerField(primary_key=True, verbose_name= 'Id de Mascota')
    tipoAnimal = models.CharField(max_length= 50, verbose_name= 'Tipo de Animal')
    detalles = models.CharField(max_length= 200, verbose_name= 'Detalles del animal')

    class Meta:
        managed = False
        db_table = 'Clientes'

class Dadosdebaja(models.Model):
    idBaja = models.IntegerField(primary_key=True, verbose_name = 'Id de Baja')
    Cliente = models.CharField(max_length= 200, verbose_name = 'Razon Baja')

    class Meta:
        managed = False
        db_table = 'Dadosdebaja'