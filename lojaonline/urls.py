from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from lojaonline_app.views import (
    UsuarioViewSet,
    CategoriaViewSet,
    ProdutoViewSet,
    CarrinhoViewSet,
    CarrinhoItemViewSet,
    PedidoViewSet,
    PedidoItemViewSet,
    VendaViewSet,
    MensagemViewSet,
    home  # Importa a view home
)

# Configura o roteador da API
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'carrinhos', CarrinhoViewSet)
router.register(r'carrinho-itens', CarrinhoItemViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'pedido-itens', PedidoItemViewSet)
router.register(r'vendas', VendaViewSet)
router.register(r'mensagens', MensagemViewSet)

# Define as URLs do projeto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', home, name='home'),  # Página inicial
]

# Configura media/static em modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
