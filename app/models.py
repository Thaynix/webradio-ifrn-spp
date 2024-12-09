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
        return self.position

class Pedidos (models.Model):
    description = models.CharField(max_length=225, verbose_name="Descrição")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Cadastrado em")

    def __str__(self):
        return self.description
    

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

# Cada episódio deve ter um título, descrição e o arquivo de áudio.
class ProgramEp(models.Model):
    title = models.CharField(max_length=100, verbose_name='titulo')
    description = models.CharField(max_length=255, verbose_name='description')
    audio = models.FileField(upload_to='audios/', verbose_name='Audio')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Cadastrado em")
    
    program = models.ForeignKey(Program, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return self.title
    
# Calendario de eventos.
class Event(models.Model):
    name = models.CharField(max_length=100, verbose_name='nome')
    date = models.DateField()
    hour = models.TimeField()
    description = models.CharField(max_length=255, verbose_name='description')

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.name













