from django.contrib import admin
from .models import Cliente, TipoProduto, Produto, Venda, ItensVenda, Pagamento

admin.site.register(Cliente)
admin.site.register(TipoProduto)
admin.site.register(Produto)
admin.site.register(Venda)
admin.site.register(ItensVenda)
admin.site.register(Pagamento)
