from django.db import models

# Create your models here.


# main/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Estudiante'),
        ('collaborator', 'Colaborador'),
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    # Campos adicionales para Estudiantes
    country = models.CharField(max_length=100, blank=True, null=True)
    university = models.CharField(max_length=200, blank=True, null=True)

    
    def __str__(self):
        return self.username


class Posts(models.Model):
    type_choices = [('ulsa','La Salle'),('ana','Anahuac'),('tec','Tecnologico de Monterrey'),('ipn','IPN'),('unam','UNAM')]
    title = models.CharField(max_length=50) #Buscar tipos de campos que hay y sus caracteristicas
    description = models.TextField(max_length=500) #Buscar lo que quiero de este dato
    university = models.CharField(max_length=4,choices=type_choices, null=True)
    user = models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

