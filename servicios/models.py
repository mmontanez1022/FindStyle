from django.db import models
from django.contrib.auth.models import User #tabla usuario xd 1.12 migraciones 

# Create your models here.
class Servicios(models.Model): #1,05
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes_productos/', null=True, blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    
    def __str__(self):
        return self.title + '- by ' + self.user.username