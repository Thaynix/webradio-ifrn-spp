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
    is_auto_generated = models.BooleanField(default=False)

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
    # CHOICE aprovado - negado - pendente
    # Campo Choice default pendente
    STATUS_CHOICES = [
        ('aprovado', 'aprovado'),
        ('negado', 'negado'),
        ('pendente', 'pendente'),
    ]
    
    singer = models.CharField(null=True,max_length=90, verbose_name="Artista/Banda")
    description = models.CharField(max_length=225, verbose_name="Nome da Música")	
    author = models.CharField(max_length=90, verbose_name="Seu Nome")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Cadastrado em")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')
    
    def __str__(self):
        return f"{self.description} - {self.singer}"


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
    

# Agenda pt.2
class Calendar(models.Model):
    COLORS_CHOICES = [
        ('#005c81', 'azul'),
        ('#d40f60', 'rosa'),
        ('#f84339', 'laranja'),
        ('#e79a32', 'amarelo'),
        ('#368986', 'verde'),
        ('#7345d6', 'roxo'),
        ('#99b333', 'verde-claro'),
    ]
    
    date = models.DateField(verbose_name="Data do programa")
    program = models.ForeignKey(Program, on_delete=models.PROTECT, null=True, blank=True)
    color = models.CharField(max_length=7, choices=COLORS_CHOICES, default='#005c81')

    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.date.strftime("%d/%m/%Y")
    














