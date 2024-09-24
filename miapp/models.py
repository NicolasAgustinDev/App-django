from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class tareas(models.Model):
    nombre=models.CharField(max_length=200)
    descripcion=models.TextField()
    done=models.BooleanField(default=False)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
