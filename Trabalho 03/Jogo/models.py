from django.db import models
from Administracao.models import Genero

class Jogo(models.Model):
    nome_do_jogo = models.CharField(max_length=100)
    data_de_lancamento = models.DateField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    sinopse = models.TextField()
    preco = models.FloatField()
    estoque_atual = models.PositiveSmallIntegerField()

    


    def __str__(self):
        return self.nome_do_jogo
