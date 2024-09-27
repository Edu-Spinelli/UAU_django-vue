from rest_framework import viewsets
from .models import Cliente, TipoProduto, Produto, Venda, ItensVenda, Pagamento
from .serializers import ClienteSerializer, TipoProdutoSerializer, ProdutoSerializer, VendaSerializer, ItensVendaSerializer, PagamentoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class TipoProdutoViewSet(viewsets.ModelViewSet):
    queryset = TipoProduto.objects.all()
    serializer_class = TipoProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

class ItensVendaViewSet(viewsets.ModelViewSet):
    queryset = ItensVenda.objects.all()
    serializer_class = ItensVendaSerializer

class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer
