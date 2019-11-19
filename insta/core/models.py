from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings

class User(AbstractUser):
    username = models.CharField('username', max_length=150, unique=True)
    nome = models.CharField(
        'Nome Completo',
        max_length=200,
        unique=False,
        null=True
    )
    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'


    def __str__(self):
        return str(self.username)

class Foto(models.Model):

    imagem = models.ImageField('Foto', upload_to='media/foto')
    legenda = models.CharField('Legenda', max_length = 2200)

    def __str__(self):
        return self.legenda

    def get_absolute_url(self):
        return reverse('foto_edit', kwargs={'pk': self.pk})


    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'

class Like(models.Model):

    usuario = models.ManyToManyField(User)
    foto = models.ManyToManyField(Foto)