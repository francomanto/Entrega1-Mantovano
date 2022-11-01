from django.db import models

class Profesional(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    especialidad = models.CharField(max_length=40)
    tel= models.IntegerField()
    
    def __str__(self):
        return f"Profesional: {self.name} {self.last_name} | Especialidad: {self.especialidad}"