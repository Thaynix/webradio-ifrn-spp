from django.db import models
from django.contrib.auth.models import User

class WarningCard(models.Model):
    COLOR_OPTIONS = [
        ('#3a7b50', 'Green'),
        ('#f8a348', 'Yellow'),
        ('#e15244', 'Red'),
        ('#3357FF', 'Blue'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=7, choices=COLOR_OPTIONS, default='Green') 

    def __str__(self):
        return self.title


class Program(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Imagem')
    name = models.CharField(max_length=100, verbose_name='Nome')
    description = models.CharField(max_length=255, verbose_name="Descrição")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Cadastrado em")

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.name