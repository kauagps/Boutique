from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    tipo = models.CharField(max_length=20, choices=[('cliente', 'Cliente'), ('admin', 'Administrador')], default='cliente')
    google_id = models.CharField(max_length=255, null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estoque = models.IntegerField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Carrinho(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrinho de {self.usuario}"


class CarrinhoItem(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"


class Pedido(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('pago', 'Pago'),
        ('cancelado', 'Cancelado'),
    ]
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario}"


class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"


class Venda(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_venda = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venda #{self.id} - Pedido {self.pedido.id}"


class Mensagem(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    lida = models.BooleanField(default=False)

    def __str__(self):
        return f"Mensagem de {self.usuario.username}"
