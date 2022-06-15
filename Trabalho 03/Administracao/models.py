from django.db import models

class Genero(models.Model):
    nome_do_genero = models.CharField(max_length=100)
 

    def __str__(self):
        return self.nome_do_genero

class Funcionario(models.Model):
    Nome = models.CharField(max_length=100)
    data_de_nascimento = models.DateField()
    email = models.EmailField()
    cpf = models.PositiveBigIntegerField()
    

    
    def __str__(self):
        return self.Nome

class Cliente(models.Model):
    Nome = models.CharField(max_length=100)
    data_de_nascimento = models.DateField()
    email = models.EmailField()
    cpf = models.PositiveBigIntegerField()
    telefone = models.CharField(max_length=100)
    endereco = models.TextField()
    

    
    def __str__(self):
        return self.Nome

class Pagamento(models.Model):
    metodo_pagamento = models.CharField(max_length=100)
 

    def __str__(self):
        return self.metodo_pagamento

