from django.contrib import admin
from .models import Cliente
from .models import Funcionario
from .models import Genero
from .models import Pagamento

admin.site.register(Cliente)
admin.site.register(Funcionario)
admin.site.register(Genero)
admin.site.register(Pagamento)