from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse

from hashlib import sha256

from .models import Usuario

def cadastro(request):
    if request.session.get('usuario'):
        return redirect('/livros/home')
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

def valida_cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        usuario = Usuario.objects.filter(email=email)

        if len(nome.strip()) == 0 or len(email.strip()) == 0:
            return redirect('/auth/cadastro/?status=1')

        if len(senha) < 6:
            return redirect('/auth/cadastro/?status=2')

        if len(usuario) > 0:  #usuário já existe
            return redirect('/auth/cadastro/?status=3')


        try:
            senha = sha256(senha.encode('utf-8')).hexdigest()
            usuario = Usuario(nome=nome, senha=senha, email=email)
            usuario.save()
            return redirect('/auth/cadastro/?status=0')
        except:
            return redirect('/auth/cadastro/?status=4')

def login(request):
    if request.session.get('usuario'):
        return redirect('/livros/home')
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    senha = sha256(senha.encode('utf-8')).hexdigest()

    usuario = Usuario.objects.filter(email=email, senha=senha)

    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect('/livros/home')

def sair(request):
    request.session.flush()
    return redirect('/auth/login/')