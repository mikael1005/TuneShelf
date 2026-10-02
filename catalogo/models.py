from django.contrib.auth.models import User
from django.db import models


class Musica(models.Model):
    STATUS_CHOICES = [
        ("OUVIDA", "Ouvida"),
        ("QUERO_OUVIR", "Quero ouvir"),
        ("OUVINDO", "Estou ouvindo"),
    ]

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="musicas",
    )
    titulo = models.CharField(max_length=120)
    artista = models.CharField(max_length=120)
    album = models.CharField(max_length=120, blank=True)
    descricao = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="QUERO_OUVIR",
    )
    nota = models.PositiveSmallIntegerField(blank=True, null=True)
    data_adicao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-data_adicao"]

    def __str__(self):
        return f"{self.titulo} - {self.artista}"
