from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm
from django.shortcuts import render, redirect
from .models import Produto, Venda, ItensVenda, Cliente, Fornecedor, Vendedor
from .forms import ClienteForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def landing(request):
    return render(request,'app/index.html')

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'app/contact_list.html', {'contacts': contacts})

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'app/contact_form.html', {'form': form})

def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'app/contact_form.html', {'form': form})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'app/contact_confirm_delete.html', {'contact': contact})

def cadastro_clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing')
    else:
        form = ClienteForm()
    return render(request, 'app/cadastro_clientes.html', {'form': form})

def demonstrativo_tabelas(request):
    clientes = Cliente.objects.all()
    fornecedores = Fornecedor.objects.all()
    produtos = Produto.objects.all()
    vendas = Venda.objects.all()
    return render(request, 'app/demonstrativo_tabelas.html', {
        'clientes': clientes,
        'fornecedores': fornecedores,
        'produtos': produtos,
        'vendas': vendas,
    })

def realizar_venda(request):
    if request.method == 'POST':
        # Lógica simplificada para processar a venda
        cliente_id = request.POST.get('cliente')
        produto_id = request.POST.get('produto')
        quantidade = request.POST.get('quantidade')
        cliente = Cliente.objects.get(idcli=cliente_id)
        produto = Produto.objects.get(idprod=produto_id)
        vendedor = Vendedor.objects.first()  # Supondo que há um vendedor padrão
        fornecedor = produto.idforn

        valor_venda = produto.valorprod * int(quantidade)
        venda = Venda.objects.create(
            codivend='12345',  # Código de venda gerado automaticamente
            idcli=cliente,
            idforn=fornecedor,
            idvende=vendedor,
            valorvend=valor_venda,
            descvend=0,
            totalvend=valor_venda,
            datavend='2023-07-19',  # Data atual
            valorcomissao=valor_venda * vendedor.porcvende / 100
        )

        ItensVenda.objects.create(
            idvend=venda,
            idprod=produto,
            valoritvend=produto.valorprod,
            qtditvend=quantidade,
            descitvend=0
        )

        return redirect('home')

    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()
    return render(request, 'app/realizar_venda.html', {
        'clientes': clientes,
        'produtos': produtos,
    })

def login_view(request):
    if request.method == "POST":
        # Criar um formulário de autenticação com os dados do POST
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Extrair username e password do formulário
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Autenticar o usuário
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Se a autenticação for bem-sucedida, fazer login e redirecionar
                login(request, user)
                return redirect('landing')
    else:
        # Se não for POST, criar um formulário vazio
        form = AuthenticationForm()
    # Renderizar a página de login com o formulário
    return render(request, 'app/login.html', {'form': form})

# View para o registro de novos usuários
def register_view(request):
    if request.method == "POST":
        # Criar um formulário de registro com os dados do POST
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Se o formulário for válido, salvar o usuário e fazer login
            user = form.save()
            login(request, user)
            return redirect('landing')
    else:
        # Se não for POST, criar um formulário vazio
        form = UserRegisterForm()
    # Renderizar a página de registro com o formulário
    return render(request, 'app/register.html', {'form': form})

# View para a página de boas-vindas

# View para o logout de usuários
def logout_view(request):
    logout(request)
    return redirect('login')
# View para listar todos os usuários
def user_list_view(request):
    users = User.objects.all()
    # Renderiza a página de lista de usuários com os dados dos usuários
    return render(request, 'app/user_list.html', {'users': users})