from django.db import models

# Create your models here.
class CategoriaProd(models.Model):
    nombre = models.CharField(max_length=100)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "categoriaProd"
        verbose_name_plural = "categoriasProd"

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    descripcion = models.TextField()
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='tienda/static/img/', blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre