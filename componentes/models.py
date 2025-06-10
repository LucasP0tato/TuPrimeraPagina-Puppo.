from django.db import models

class Procesador(models.Model):
    nombre = models.CharField(max_length=100)
    velocidad = models.DecimalField(max_digits=4, decimal_places=2)
    nucleos = models.IntegerField()

    def __str__(self):
        return self.nombre

class PlacaVideo(models.Model):
    nombre = models.CharField(max_length=100)
    memoria = models.IntegerField()  # en MB
    fabricante = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Motherboard(models.Model):
    nombre = models.CharField(max_length=100)
    socket = models.CharField(max_length=50)
    chipset = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre