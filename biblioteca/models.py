from django.db import models

# Create your models here.
class Ciudad(models.Model):
    nombre = models.CharField(max_length=80)
    Campo01 = models.CharField(max_length=80)
    Campo02 = models.CharField(max_length=80)

class Biblioteca(models.Model):
    nombre = models.CharField(max_length=80)
    direccion = models.CharField(max_length=100)
    ciudad_id = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    telefono = models.IntegerField()

class Genero(models.Model):
    nombre = models.CharField(max_length=50)

class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=80)
    genero_id = models.ForeignKey(Genero, on_delete=models.CASCADE)
    isbn = models.IntegerField()
    descripcion = models.TextField(max_length=400)
    biblioteca_id = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)