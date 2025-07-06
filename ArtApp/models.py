from django.db import models

# Create your models here.
class SolicitudComision(models.Model):
    TIPO_CHOICES = [
        ('Retrato simple', 'Retrato simple'),
        ('Cuerpo completo', 'Cuerpo completo'),
        ('Diseño de personaje', 'Diseño de personaje'),
        ('Pareja', 'Pareja / Duo'),
        ('NSFW', 'NSFW Personalizado'),
    ]

    nombre = models.CharField(max_length=50)
    email = models.EmailField(blank=False, null=False)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    descripcion = models.TextField(max_length=500, blank=True, null=True)
    referencias = models.URLField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre