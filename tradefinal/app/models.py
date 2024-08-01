from django.db import models

# Modelo para Contatos
class Contact(models.Model):
    # Campo para o nome do contato
    name = models.CharField(max_length=100)
    # Campo para o carro do contato
    carro = models.CharField(max_length=100)
    # Campo para o serviço relacionado ao contato
    servico = models.CharField(max_length=100)
    # Campo para o telefone do contato
    telefone = models.CharField(max_length=100)
    # Campo para a data e hora de submissão (preenchido automaticamente)
    submiited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Retorna o nome do contato quando o objeto é convertido para string
        return self.name

# Modelo para Vendedores
class Vendedor(models.Model):
    # Chave primária autoincrementada
    idvende = models.AutoField(primary_key=True)
    # Código do vendedor
    codivende = models.CharField(max_length=10)
    # Nome do vendedor
    nomevende = models.CharField(max_length=100)
    # Razão social do vendedor
    razasocvende = models.CharField(max_length=100)
    # Telefone do vendedor
    fonevende = models.CharField(max_length=20)
    # Porcentagem de comissão do vendedor
    porcvende = models.FloatField()

    class Meta:
        # Define o nome da tabela no banco de dados
        db_table = 'vendedor'

# Modelo para Produtos
class Produto(models.Model):
    # Chave primária autoincrementada
    idprod = models.AutoField(primary_key=True)
    # Código do produto
    codiprod = models.CharField(max_length=20)
    # Descrição do produto
    descprod = models.CharField(max_length=100)
    # Valor do produto
    valorprod = models.FloatField()
    # Situação do produto (ativo/inativo)
    situprod = models.CharField(max_length=1)
    # Chave estrangeira para o fornecedor
    idforn = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)

    class Meta:
        # Define o nome da tabela no banco de dados
        db_table = 'produto'

# Modelo para Fornecedores
class Fornecedor(models.Model):
    # Chave primária autoincrementada
    idforn = models.AutoField(primary_key=True)
    # Código do fornecedor
    codiforn = models.CharField(max_length=10)
    # Nome do fornecedor
    nomeforn = models.CharField(max_length=100)
    # Razão social do fornecedor
    razasocforn = models.CharField(max_length=100)
    # Telefone do fornecedor
    foneforn = models.CharField(max_length=20)

    class Meta:
        # Define o nome da tabela no banco de dados
        db_table = 'fornecedor'

# Modelo para Clientes
class Cliente(models.Model):
    # Chave primária autoincrementada
    idcli = models.AutoField(primary_key=True)
    # Código do cliente
    codcli = models.CharField(max_length=10)
    # Nome do cliente
    nomecli = models.CharField(max_length=100)
    # Razão social do cliente
    razasoccli = models.CharField(max_length=100)
    # Data de cadastro do cliente
    datacli = models.DateField()
    # CNPJ do cliente
    cnpjcli = models.CharField(max_length=20)
    # Telefone do cliente
    fonecli = models.CharField(max_length=20)
    # Cidade do cliente
    cidcli = models.CharField(max_length=50)
    # Estado do cliente
    estcli = models.CharField(max_length=100)

    class Meta:
        # Define o nome da tabela no banco de dados
        db_table = 'cliente'

# Modelo para Itens de Venda
class ItensVenda(models.Model):
    # Chave primária autoincrementada
    iditvend = models.AutoField(primary_key=True)
    # Chave estrangeira para a venda
    idvend = models.ForeignKey('Venda', on_delete=models.CASCADE)
    # Chave estrangeira para o produto
    idprod = models.ForeignKey('Produto', on_delete=models.CASCADE)
    # Valor do item na venda
    valoritvend = models.FloatField()
    # Quantidade do item vendido
    qtditvend = models.IntegerField()
    # Desconto aplicado ao item
    descitvend = models.FloatField()

    class Meta:
        # Define o nome da tabela no banco de dados
        db_table = 'itensvenda'

# Modelo para Vendas
class Venda(models.Model):
    # Chave primária autoincrementada
    idvend = models.AutoField(primary_key=True)
    # Código da venda
    codivend = models.CharField(max_length=10)
    # Chave estrangeira para o cliente
    idcli = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    # Chave estrangeira para o fornecedor
    idforn = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)
    # Chave estrangeira para o vendedor
    idvende = models.ForeignKey('Vendedor', on_delete=models.CASCADE)
    # Valor total da venda
    valorvend = models.FloatField()
    # Desconto total aplicado à venda
    descvend = models.FloatField()
    # Valor total da venda após desconto
    totalvend = models.FloatField()
    # Data da venda
    datavend = models.DateField()
    # Valor da comissão do vendedor
    valorcomissao = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        # Define o nome da tabela no banco de dados
        db_table = 'venda'

# Modelo para Backup de Clientes
class ClienteBkp(models.Model):
    # Chave primária autoincrementada
    idcli = models.AutoField(primary_key=True)
    # Código do cliente
    codcli = models.CharField(max_length=10)
    # Nome do cliente
    nomecli = models.CharField(max_length=100)
    # Razão social do cliente
    razasoccli = models.CharField(max_length=100)
    # Data de cadastro do cliente
    datacli = models.DateField()
    # CNPJ do cliente
    cnpjcli = models.CharField(max_length=20)
    # Telefone do cliente
    fonecli = models.CharField(max_length=20)
    # Cidade do cliente
    cidcli = models.CharField(max_length=50)
    # Estado do cliente
    estcli = models.CharField(max_length=100)

    class Meta:
        # Define o nome da tabela no banco de dados
        db_table = 'clientesbkp'