from django.db import models

# Create your models here.
class Tienda(models.Model):
    nombre=models.CharField(max_length=100)
    tipo=models.CharField(max_length=100)
    ubicacion=models.CharField(max_length=100)
    horario=models.CharField(max_length=100)
    foto=models.ImageField(upload_to='img_tiendas/', blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name='Tienda'
        verbose_name_plural='Tiendas'

class Empleado(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    puesto=models.CharField(max_length=100)
    telefono=models.CharField(max_length=12)
    salario=models.DecimalField(max_digits=8, decimal_places=2)
    tienda=models.ForeignKey(Tienda, on_delete=models.CASCADE, related_name='empleados')

    def __str__(self):
        return (f'{self.nombre} {self.tienda.nombre}')
    
    class Meta:
        verbose_name='Empleado'
        verbose_name_plural='Empleados'