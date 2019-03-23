from django.contrib.auth.models import User
from django.db import models


class Produto(models.Model):

    nome = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )

    descricao = models.TextField(
        max_length=30,
        null=False,
        blank=False
    )

    qtd = models.PositiveIntegerField(
        null=False,
        blank=False
    )

    preco = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False
    )

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.id, self.nome)

    objetos = models.Manager()
