from django.db import models

# Create your models here.


class Alumno(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    nombre2 = models.CharField(max_length=50)
    iD = models.PositiveSmallIntegerField()
    edad = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.edad)
