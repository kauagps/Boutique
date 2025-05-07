# SERIALIZERS
from rest_framework import serializers
from .models import Usuario, Categoria, Produto, Carrinho, CarrinhoItem, Pedido, PedidoItem, Venda, Mensagem

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class CarrinhoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarrinhoItem
        fields = '__all__'

class CarrinhoSerializer(serializers.ModelSerializer):
    itens = CarrinhoItemSerializer(many=True, read_only=True)

    class Meta:
        model = Carrinho
        fields = '__all__'

class PedidoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoItem
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    itens = PedidoItemSerializer(many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = '__all__'

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = '__all__'

class MensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensagem
        fields = '__all__'
