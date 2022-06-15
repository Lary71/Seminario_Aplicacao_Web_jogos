from django.contrib import admin
from .models import Venda
from Jogo.models import Jogo

class Display(admin.ModelAdmin):
    list_display = ('Jogovendido', 'Data_da_venda', 'Venda_Realizada_Por', 'Preco', 'Nome_Cliente')

    def jogo_vendido(self, instance):
        return instance.Jogovendido.nome_do_jogo
admin.site.register(Venda, Display)