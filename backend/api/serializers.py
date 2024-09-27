from rest_framework import serializers
from .models import Cliente, TipoProduto, Produto, Venda, ItensVenda, Pagamento

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class TipoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProduto
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = '__all__'

class ItensVendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensVenda
        fields = '__all__'

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__'
