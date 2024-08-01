from django.contrib import admin
from .models import Vendedor, Fornecedor, Produto, Cliente, ClienteBkp, Venda, ItensVenda

admin.site.register(Vendedor)
admin.site.register(Fornecedor)
admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(ClienteBkp)
admin.site.register(Venda)
admin.site.register(ItensVenda)
# Register your models here.
