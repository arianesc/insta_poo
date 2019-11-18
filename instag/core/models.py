from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField('Nome de usuário', max_length=150, unique=True)
    nome = models.CharField(
        'Nome Completo',
        max_length=200,
        unique=False,
        null=True
    )
    #email = models.EmailField('E-mail', max_length = 200)
    REQUIRED_FIELDS = ['username', 'email']
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return str(self.username)

class Foto(models.Model):

    imagem = models.ImageField('Foto', upload_to='media/foto')
    legenda = models.CharField('Legenda', max_length = 2200)

    def __str__(self):
        return self.legenda

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'

class Like(models.Model):

    usuario = models.ManyToManyField(User)
    foto = models.ManyToManyField(Foto)