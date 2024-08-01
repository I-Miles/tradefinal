# Importações necessárias do Django e dos modelos/formulários locais
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Contact, Produto, Venda, ItensVenda, Cliente, Fornecedor, Vendedor
from .forms import ContactForm, ClienteForm, UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


# View para a página inicial (landing page)
def landing(request):
    # Renderiza o template 'app/index.html'
    return render(request, 'app/index.html')


# View para listar todos os contatos
def contact_list(request):
    # Busca todos os contatos do banco de dados
    contacts = Contact.objects.all()
    # Renderiza o template 'app/contact_list.html' passando os contatos como contexto
    return render(request, 'app/contact_list.html', {'contacts': contacts})


# View para criar um novo contato
def contact_create(request):
    if request.method == 'POST':
        # Se o método for POST, cria um formulário com os dados enviados
        form = ContactForm(request.POST)
        if form.is_valid():
            # Se o formulário for válido, salva o novo contato
            form.save()
            # Redireciona para a lista de contatos
            return redirect('contact_list')
    else:
        # Se o método não for POST, cria um formulário em branco
        form = ContactForm()
    # Renderiza o template 'app/contact_form.html' com o formulário
    return render(request, 'app/contact_form.html', {'form': form})


# View para atualizar um contato existente
def contact_update(request, pk):
    # Busca o contato pelo ID (pk) ou retorna um erro 404 se não encontrar
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        # Se o método for POST, cria um formulário com os dados enviados e a instância do contato
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            # Se o formulário for válido, salva as alterações
            form.save()
            # Redireciona para a lista de contatos
            return redirect('contact_list')
    else:
        # Se o método não for POST, cria um formulário com os dados do contato
        form = ContactForm(instance=contact)
    # Renderiza o template 'app/contact_form.html' com o formulário
    return render(request, 'app/contact_form.html', {'form': form})


# View para excluir um contato
def contact_delete(request, pk):
    # Busca o contato pelo ID (pk) ou retorna um erro 404 se não encontrar
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        # Se o método for POST, exclui o contato
        contact.delete()
        # Redireciona para a lista de contatos
        return redirect('contact_list')
    # Se o método não for POST, renderiza uma página de confirmação
    return render(request, 'app/contact_confirm_delete.html', {'contact': contact})


# View para cadastrar novos clientes
def cadastro_clientes(request):
    if request.method == 'POST':
        # Se o método for POST, cria um formulário com os dados enviados
        form = ClienteForm(request.POST)
        if form.is_valid():
            # Se o formulário for válido, salva o novo cliente
            form.save()
            # Redireciona para a página inicial
            return redirect('landing')
    else:
        # Se o método não for POST, cria um formulário em branco
        form = ClienteForm()
    # Renderiza o template 'app/cadastro_clientes.html' com o formulário
    return render(request, 'app/cadastro_clientes.html', {'form': form})


# View para exibir tabelas demonstrativas
def demonstrativo_tabelas(request):
    # Busca todos os clientes, fornecedores, produtos e vendas do banco de dados
    clientes = Cliente.objects.all()
    fornecedores = Fornecedor.objects.all()
    produtos = Produto.objects.all()
    vendas = Venda.objects.all()
    # Renderiza o template 'app/demonstrativo_tabelas.html' com os dados
    return render(request, 'app/demonstrativo_tabelas.html', {
        'clientes': clientes,
        'fornecedores': fornecedores,
        'produtos': produtos,
        'vendas': vendas,
    })


# View para realizar uma venda
def realizar_venda(request):
    if request.method == 'POST':
        # Obtém os dados do formulário
        cliente_id = request.POST.get('cliente')
        produto_id = request.POST.get('produto')
        quantidade = request.POST.get('quantidade')

        # Busca os objetos relacionados
        cliente = Cliente.objects.get(idcli=cliente_id)
        produto = Produto.objects.get(idprod=produto_id)
        vendedor = Vendedor.objects.first()  # Pega o primeiro vendedor (isso pode precisar ser modificado)
        fornecedor = produto.idforn


        # Calcula o valor da venda
        valor_venda = produto.valorprod * int(quantidade)

        # Cria o objeto Venda
        venda = Venda.objects.create(
            codivend='12345',  # Este código deveria ser gerado dinamicamente
            idcli=cliente,
            idforn=fornecedor,
            idvende=vendedor,
            valorvend=valor_venda,
            descvend=0,
            totalvend=valor_venda,
            datavend='2023-07-19',  # Esta data deveria ser a data atual
            valorcomissao=valor_venda * vendedor.porcvende / 100
        )

        # Cria o objeto ItensVenda
        ItensVenda.objects.create(
            idvend=venda,
            idprod=produto,
            valoritvend=produto.valorprod,
            qtditvend=quantidade,
            descitvend=0
        )

        # Redireciona para a página inicial após a venda
        return redirect('landing')

    # Se o método não for POST, busca todos os clientes e produtos
    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()
    # Renderiza o template 'app/realizar_venda.html' com os dados
    return render(request, 'app/realizar_venda.html', {
        'clientes': clientes,
        'produtos': produtos,
    })


# View para login de usuário
def login_view(request):
    if request.method == "POST":
        # Se o método for POST, cria um formulário de autenticação com os dados enviados
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Se o formulário for válido, extrai o username e password
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Tenta autenticar o usuário
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Se a autenticação for bem-sucedida, faz o login e redireciona
                login(request, user)
                return redirect('landing')
    else:
        # Se o método não for POST, cria um formulário em branco
        form = AuthenticationForm()
    # Renderiza o template 'app/login.html' com o formulário
    return render(request, 'app/login.html', {'form': form})


# View para registro de novo usuário
def register_view(request):
    if request.method == "POST":
        # Se o método for POST, cria um formulário de registro com os dados enviados
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Se o formulário for válido, salva o novo usuário e faz login
            user = form.save()
            login(request, user)
            return redirect('landing')
    else:
        # Se o método não for POST, cria um formulário em branco
        form = UserRegisterForm()
    # Renderiza o template 'app/register.html' com o formulário
    return render(request, 'app/register.html', {'form': form})


# View para logout de usuário
def logout_view(request):
    # Faz o logout do usuário
    logout(request)
    # Redireciona para a página de login
    return redirect('login')


# View para listar todos os usuários
def user_list_view(request):
    # Busca todos os usuários do banco de dados
    users = User.objects.all()
    # Renderiza o template 'app/user_list.html' com a lista de usuários
    return render(request, 'app/user_list.html', {'users': users})