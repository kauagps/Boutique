from django.shortcuts import render
# ecommerce/views.py
from rest_framework import viewsets
from .models import Usuario, Categoria, Produto, Carrinho, CarrinhoItem, Pedido, PedidoItem, Venda, Mensagem
from .serializers import (
    UsuarioSerializer,
    CategoriaSerializer,
    ProdutoSerializer,
    CarrinhoSerializer,
    CarrinhoItemSerializer,
    PedidoSerializer,
    PedidoItemSerializer,
    VendaSerializer,
    MensagemSerializer
)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class CarrinhoViewSet(viewsets.ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer

class CarrinhoItemViewSet(viewsets.ModelViewSet):
    queryset = CarrinhoItem.objects.all()
    serializer_class = CarrinhoItemSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoItemViewSet(viewsets.ModelViewSet):
    queryset = PedidoItem.objects.all()
    serializer_class = PedidoItemSerializer

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

class MensagemViewSet(viewsets.ModelViewSet):
    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer

def home(request):
    return render(request, 'lojaonline_app/home.html')