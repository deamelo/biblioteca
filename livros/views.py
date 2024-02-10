from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Emprestimos, Livros, Categoria

from usuarios.models import Usuario

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        livros = Livros.objects.filter(usuario = usuario)
        return render(request, 'home.html', {'livros': livros})
    else:
        return redirect('/auth/login/?status=2')


def ver_livro(request, id):
    if request.session.get('usuario'):
        livro = Livros.objects.get(id = id)
        if request.session.get('usuario') == livro.usuario.id:
            categoria = Categoria.objects.filter(usuario = request.session.get('usuario'))
            emprestimo = Emprestimos.objects.filter(livro = livro)
            return render(request, 'ver_livro.html', {'livro':livro, 'categoria': categoria, 'emprestimo': emprestimo})
        else:
            return HttpResponse('erro')
    return redirect('/auth/login/?status=2')