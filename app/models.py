from django.db import models
from django.contrib.auth.models import User

# Carrosel de imagens
class ImageCarousel(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Carousel Imagem')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="publicado em")

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title

# Cards de avisos na pagina inicial
class WarningCard(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class AboutRadio(models.Model):
    text = models.TextField(unique=True, max_length=1500, verbose_name="Sobre")
    image = models.ImageField(unique=True, null=True, blank=True, upload_to='images/')

# Cards que mostram a equipe da rádio
class ProfileCard(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='imagem')
    position = models.CharField(max_length=100, verbose_name="Posição")
    name = models.CharField(max_length=100, verbose_name="Nome")
    description = models.CharField(max_length=255, verbose_name="Descrição")

    class Meta:
        ordering = ['-position']

    def __str__(self):
        return self.name



# Cards dos programas na pagina de programação
class Program(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Imagem')
    name = models.CharField(max_length=100, verbose_name='Nome')
    description = models.CharField(max_length=255, verbose_name="Descrição")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Cadastrado em")

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.name















