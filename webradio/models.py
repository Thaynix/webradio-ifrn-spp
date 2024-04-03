from django.db import models
from django.contrib.auth.models import User


class Program(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='imagem')
    name = models.CharField(max_length=100, verbose_name='Nome')
    description = models.CharField(max_length=255, verbose_name="Descrição")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Cadastradado em")
    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.name
    