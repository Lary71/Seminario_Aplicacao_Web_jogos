from tkinter import CASCADE
from django.db import models
from Jogo.models import Jogo
from Administracao.models import Funcionario
from Administracao.models import Pagamento
from Administracao.models import Cliente

class Venda(models.Model):
    Jogovendido = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    Venda_Realizada_Por = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    Data_da_venda = models.DateTimeField()
    Nome_Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Preco = models.FloatField()
    Metodo_de_Pagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE)
    

    
    def __str__(self):
        return self.Jogovendido.nome_do_jogo
