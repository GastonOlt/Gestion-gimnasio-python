from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    servicios = models.ManyToManyField(Servicio, blank=True)
    editado = models.DateTimeField(auto_now=True)   
    imagen = models.ImageField(upload_to="clientes/",blank=True, null=True)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    def total_servicios(self):
        total = sum(servicio.precio for servicio in self.servicios.all())
        return total
