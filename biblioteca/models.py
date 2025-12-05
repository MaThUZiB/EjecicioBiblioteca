from django.db import models

# Create your models here.
class Ciudad(models.Model):
    nombre = models.CharField(max_length=80)
    campo01 = models.CharField(max_length=80)
    campo02 = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre
    
class Biblioteca(models.Model):
    nombre = models.CharField(max_length=80)
    direccion = models.CharField(max_length=100)
    ciudad_id = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=80)
    genero_id = models.ForeignKey(Genero, on_delete=models.CASCADE)
    isbn = models.IntegerField()
    descripcion = models.TextField(max_length=400)
    biblioteca_id = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo