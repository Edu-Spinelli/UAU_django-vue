from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, unique=True)
    saldo_devedor = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nome

class TipoProduto(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoProduto, on_delete=models.CASCADE)  # Ligação com o tipo de produto
    preco_pago = models.DecimalField(max_digits=10, decimal_places=2)  # Preço pago ao adquirir o produto
    quantidade = models.IntegerField()  # Quantidade em estoque

    def __str__(self):
        return self.nome

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Cliente que realizou a compra
    data_venda = models.DateField()  # Data da venda
    num_parcelas = models.IntegerField(default=1)  # Número de parcelas acordadas
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Valor total da venda, será calculado
    valor_restante = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Valor restante a ser pago

    def __str__(self):
        return f'Venda {self.id} - Cliente {self.cliente.nome}'

    def calcular_valor_total(self):
        # Calcula o valor total da venda somando os itens de venda
        total = sum(item.preco_venda * item.quantidade for item in self.itens.all())
        self.valor_total = total
        self.valor_restante = total
        self.save()
        return total

    def registrar_pagamento(self, valor_pago):
        # Verifica se o valor pago é maior que o valor restante
        if valor_pago > self.valor_restante:
            raise ValueError(f'O valor pago ({valor_pago}) não pode ser maior que o valor restante ({self.valor_restante}).')

        # Subtrai o valor pago do valor restante
        self.valor_restante -= valor_pago
        if self.valor_restante < 0:
            self.valor_restante = 0  # Evita valores negativos

        # Atualiza o saldo devedor do cliente
        self.cliente.saldo_devedor -= valor_pago
        if self.cliente.saldo_devedor < 0:
            self.cliente.saldo_devedor = 0  # Evita valores negativos

        self.cliente.save()
        self.save()


class ItensVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens')  # Ligação com a venda
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)  # Produto vendido
    quantidade = models.IntegerField()  # Quantidade de produtos vendidos
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)  # Preço de venda do produto

    def __str__(self):
        return f'{self.quantidade}x {self.produto.nome} - Venda {self.venda.id}'

    def save(self, *args, **kwargs):
            # Verifica se há estoque suficiente para a venda
            if self.produto.quantidade < self.quantidade:
                raise ValueError('Quantidade em estoque insuficiente para realizar a venda.')

            # Diminui a quantidade no estoque do produto
            self.produto.quantidade -= self.quantidade
            self.produto.save()

            # Atualiza o valor total da venda ao adicionar um item
            super().save(*args, **kwargs)
            self.venda.calcular_valor_total()

            # Atualiza o saldo devedor do cliente com o valor dos itens adicionados
            total_item_venda = self.preco_venda * self.quantidade
            self.venda.cliente.saldo_devedor += total_item_venda
            self.venda.cliente.save()


class Pagamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Cliente que fez o pagamento
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='pagamentos')  # Venda à qual o pagamento está relacionado
    valor = models.DecimalField(max_digits=10, decimal_places=2)  # Valor pago pelo cliente
    data_pagamento = models.DateField(auto_now_add=True)  # Data do pagamento

    def __str__(self):
        return f'Pagamento {self.id} - Venda {self.venda.id} - Cliente {self.cliente.nome}'

    def save(self, *args, **kwargs):
        # Verifica se a venda está associada ao cliente
        if self.venda.cliente != self.cliente:
            raise ValueError('O cliente no pagamento não corresponde ao cliente na venda.')
        
        # Ao salvar o pagamento, atualiza o valor restante da venda e o saldo do cliente
        super().save(*args, **kwargs)
        self.venda.registrar_pagamento(self.valor)
