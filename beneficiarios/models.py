from django.db import models


class Beneficiario(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    comunidade = models.CharField(max_length=100)
    data_cadastro = models.DateField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome