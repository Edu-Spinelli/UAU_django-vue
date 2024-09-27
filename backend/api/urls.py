from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, TipoProdutoViewSet, ProdutoViewSet, VendaViewSet, ItensVendaViewSet, PagamentoViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'tipo-produto', TipoProdutoViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'vendas', VendaViewSet)
router.register(r'itens-venda', ItensVendaViewSet)
router.register(r'pagamentos', PagamentoViewSet)

urlpatterns = router.urls
