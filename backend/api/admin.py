from django.contrib import admin
from .models import Perfume, Cliente, Venda, ItemVenda, Pagamento

admin.site.register(Perfume)
admin.site.register(Cliente)
admin.site.register(Venda)
admin.site.register(ItemVenda)
admin.site.register(Pagamento)