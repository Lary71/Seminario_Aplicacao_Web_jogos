from django.contrib import admin
from .models import Jogo


class Display(admin.ModelAdmin):
    list_display = ('nome_do_jogo', 'preco', 'estoque_atual')

admin.site.register(Jogo, Display)