from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    carro = models.CharField(max_length=100)
    servico = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    submiited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Vendedor(models.Model):
    idvende = models.AutoField(primary_key=True)
    codivende = models.CharField(max_length=10)
    nomevende = models.CharField(max_length=100)
    razasocvende = models.CharField(max_length=100)
    fonevende = models.CharField(max_length=20)
    porcvende = models.FloatField()

    class Meta:
        db_table = 'vendedor'


class Produto(models.Model):
    idprod = models.AutoField(primary_key=True)
    codiprod = models.CharField(max_length=20)
    descprod = models.CharField(max_length=100)
    valorprod = models.FloatField()
    situprod = models.CharField(max_length=1)
    idforn = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)

    class Meta:
        db_table = 'produto'


class Fornecedor(models.Model):
    idforn = models.AutoField(primary_key=True)
    codiforn = models.CharField(max_length=10)
    nomeforn = models.CharField(max_length=100)
    razasocforn = models.CharField(max_length=100)
    foneforn = models.CharField(max_length=20)

    class Meta:
        db_table = 'fornecedor'


class Cliente(models.Model):
    idcli = models.AutoField(primary_key=True)
    codcli = models.CharField(max_length=10)
    nomecli = models.CharField(max_length=100)
    razasoccli = models.CharField(max_length=100)
    datacli = models.DateField()
    cnpjcli = models.CharField(max_length=20)
    fonecli = models.CharField(max_length=20)
    cidcli = models.CharField(max_length=50)
    estcli = models.CharField(max_length=100)

    class Meta:
        db_table = 'cliente'


class ItensVenda(models.Model):
    iditvend = models.AutoField(primary_key=True)
    idvend = models.ForeignKey('Venda', on_delete=models.CASCADE)
    idprod = models.ForeignKey('Produto', on_delete=models.CASCADE)
    valoritvend = models.FloatField()
    qtditvend = models.IntegerField()
    descitvend = models.FloatField()

    class Meta:
        db_table = 'itensvenda'


class Venda(models.Model):
    idvend = models.AutoField(primary_key=True)
    codivend = models.CharField(max_length=10)
    idcli = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    idforn = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)
    idvende = models.ForeignKey('Vendedor', on_delete=models.CASCADE)
    valorvend = models.FloatField()
    descvend = models.FloatField()
    totalvend = models.FloatField()
    datavend = models.DateField()
    valorcomissao = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'venda'


class ClienteBkp(models.Model):
    idcli = models.AutoField(primary_key=True)
    codcli = models.CharField(max_length=10)
    nomecli = models.CharField(max_length=100)
    razasoccli = models.CharField(max_length=100)
    datacli = models.DateField()
    cnpjcli = models.CharField(max_length=20)
    fonecli = models.CharField(max_length=20)
    cidcli = models.CharField(max_length=50)
    estcli = models.CharField(max_length=100)

    class Meta:
        db_table = 'clientesbkp'
