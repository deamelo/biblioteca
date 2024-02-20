from django.db.models import Q
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Emprestimos, Livros, Categoria
from .forms import CadastroLivro, CategoriaLivro

from usuarios.models import Usuario

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        status_categoria = request.GET.get('cadastro_categoria')
        livros = Livros.objects.filter(usuario = usuario)
        total_livros = livros.count()
        form = CadastroLivro()
        form.fields['usuario'].initial = request.session['usuario']
        form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)
        form_categoria = CategoriaLivro()
        usuarios = Usuario.objects.all()

        emprestar = Livros.objects.filter(usuario = usuario).filter(emprestado = False)
        emprestados = Livros.objects.filter(usuario = usuario).filter(emprestado = True)

        return render(request, 'home.html',
            {
                'livros': livros,
                'usuario_logado': request.session.get('usuario'),
                'form':form,
                'status_categoria': status_categoria,
                'form_categoria': form_categoria,
                'usuarios': usuarios,
                'emprestar': emprestar,
                'total_livros': total_livros,
                'emprestados': emprestados,
            })
    else:
        return redirect('/auth/login/?status=2')


def ver_livro(request, id):
    if request.session.get('usuario'):
        livro = Livros.objects.get(id = id)
        if request.session.get('usuario') == livro.usuario.id:
            usuario = Usuario.objects.get(id = request.session['usuario'])
            categoria_livro = Categoria.objects.filter(usuario = request.session.get('usuario'))
            emprestimo = Emprestimos.objects.filter(livro = livro)
            form = CadastroLivro()
            form.fields['usuario'].initial = request.session['usuario']
            form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)
            form_categoria = CategoriaLivro()
            usuarios = Usuario.objects.all()

            emprestar = Livros.objects.filter(usuario = usuario).filter(emprestado = False)
            emprestados = Livros.objects.filter(usuario = usuario).filter(emprestado = True)

            return render(request, 'ver_livro.html',
                {
                    'livro':livro,
                    'categoria_livro': categoria_livro,
                    'emprestimo': emprestimo,
                    'usuario_logado': request.session.get('usuario'),
                    'form':form,
                    'id_livro': id,
                    'form_categoria': form_categoria,
                    'usuarios': usuarios,
                    'emprestar': emprestar,
                    'emprestados': emprestados,
                }
            )
        else:
            return HttpResponse('erro')
    return redirect('/auth/login/?status=2')

def cadastrar_livro(request):
    if request.method == 'POST':
        form = CadastroLivro(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/livros/home')
        else:
            return HttpResponse('Dados Inválidos')

def excluir_livro(request, id):
    livro = Livros.objects.get(id=id).delete()
    return redirect('/livros/home')

def cadastrar_categoria(request):
    form = CategoriaLivro(request.POST)
    nome = form.data['nome']
    descricao = form.data['descricao']
    id_usuario = request.POST.get('usuario')
    if int(id_usuario) == int(request.session.get('usuario')):
        usuario = Usuario.objects.get(id=id_usuario)
        categoria = Categoria(nome = nome, descricao = descricao, usuario = usuario)
        categoria.save()
        return redirect('/livros/home?cadastro_categoria=1')
    else:
        return HttpResponse('erro')


def cadastrar_emprestimo(request):
    if request.method == 'POST':
        nome_solicitante = request.POST.get('nome_solicitante')
        solicitante_anonimo = request.POST.get('solicitante_anonimo')
        livro_emprestado = request.POST.get('livro_emprestado')
        if solicitante_anonimo:
            emprestimo = Emprestimos(solicitante_anonimo = solicitante_anonimo, livro_id = livro_emprestado)
        else:
            emprestimo = Emprestimos(nome_solicitante_id = nome_solicitante, livro_id = livro_emprestado)
        emprestimo.save()
        livro = Livros.objects.get(id=livro_emprestado)
        livro.emprestado = True
        livro.save()
        return redirect('/livros/home')

def devolver_livro(request):
    id = request.POST.get('id_devolucao')
    devolucao = Livros.objects.get(id=id)
    emprestimo = Emprestimos.objects.get(Q(livro = devolucao) & Q(data_devolucao = None))
    emprestimo.data_devolucao = datetime.now()
    emprestimo.save()
    devolucao.emprestado = False
    devolucao.save()
    return redirect('/livros/home')

def editar_livro(request):
    livro_id = request.POST.get('livro_id')
    nome = request.POST.get('nome')
    autor = request.POST.get('autor')
    co_autor = request.POST.get('co_autor')
    categoria_id = request.POST.get('categoria_id')

    categoria = Categoria.objects.get(id = categoria_id)
    print('categoria_id:', categoria_id)
    print('categoria:', categoria)

    livro = Livros.objects.get(id=livro_id)

    if livro.usuario.id == request.session['usuario']:
        livro.nome = nome
        livro.autor = autor
        livro.co_autor = co_autor
        livro.categoria = categoria
        livro.save()
        return redirect(f'/livros/ver_livro/{livro_id}')
    else:
        return redirect('/auth/sair')

def meus_emprestimos(request):
    usuario = Usuario.objects.get(id = request.session['usuario'])
    emprestimos = Emprestimos.objects.filter(nome_solicitante = usuario)

    form = CadastroLivro()
    form.fields['usuario'].initial = request.session['usuario']
    form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)
    form_categoria = CategoriaLivro()

    return render(request, 'meus_emprestimos.html', {'usuario_logado': request.session['usuario'], 'emprestimos': emprestimos, 'form': form, 'form_categoria': form_categoria})

def avaliacao(request):
    id_emprestimo = request.POST.get('id_emprestimo')
    opcoes = request.POST.get('opcoes')
    id_livro = request.POST.get('id_livro')

    emprestimo = Emprestimos.objects.get(id = id_emprestimo)
    if emprestimo.livro.usuario.id == request.session['usuario']:
        emprestimo.avaliacao = opcoes
        emprestimo.save()
        return redirect(f'/livros/ver_livro/{id_livro}')
    else:
        return redirect('/auth/sair')