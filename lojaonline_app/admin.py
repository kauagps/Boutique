from django.utils.html import format_html
from django.contrib import admin
from .models import (
    Usuario, Categoria, Produto,
    Carrinho, CarrinhoItem, Pedido, PedidoItem,
    Venda, Mensagem
)

admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Carrinho)
admin.site.register(CarrinhoItem)
admin.site.register(Pedido)
admin.site.register(PedidoItem)
admin.site.register(Venda)
admin.site.register(Mensagem)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'ativo', 'categoria', 'preview_imagem')

    def preview_imagem(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" style="max-height: 80px;" />', obj.imagem.url)
        return "Sem imagem"

    preview_imagem.short_description = 'Imagem'
