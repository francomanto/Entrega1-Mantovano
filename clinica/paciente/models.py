from django.db import models

class Paciente(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    dni = models.IntegerField()
    email = models.EmailField()
    tel= models.IntegerField()
    
    def __str__(self):
        return f"Paciente: {self.name} {self.last_name} | dni: {self.dni}"