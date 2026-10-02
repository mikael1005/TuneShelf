from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MusicaForm
from .models import Musica


def cadastro(request):
    if request.user.is_authenticated:
        return redirect("catalogo:lista")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, "Conta criada com sucesso!")
            return redirect("catalogo:lista")
    else:
        form = UserCreationForm()

    return render(request, "registration/cadastro.html", {"form": form})


@login_required
def lista_musicas(request):
    musicas = Musica.objects.filter(usuario=request.user)
    return render(request, "catalogo/lista.html", {"musicas": musicas})


@login_required
def adicionar_musica(request):
    if request.method == "POST":
        form = MusicaForm(request.POST)
        if form.is_valid():
            musica = form.save(commit=False)
            musica.usuario = request.user
            musica.save()
            messages.success(request, "Música adicionada ao seu catálogo!")
            return redirect("catalogo:lista")
    else:
        form = MusicaForm()

    return render(
        request,
        "catalogo/formulario.html",
        {"form": form, "titulo_pagina": "Adicionar música", "botao": "Salvar música"},
    )


@login_required
def editar_musica(request, pk):
    musica = get_object_or_404(Musica, pk=pk, usuario=request.user)

    if request.method == "POST":
        form = MusicaForm(request.POST, instance=musica)
        if form.is_valid():
            form.save()
            messages.success(request, "Música atualizada com sucesso!")
            return redirect("catalogo:lista")
    else:
        form = MusicaForm(instance=musica)

    return render(
        request,
        "catalogo/formulario.html",
        {"form": form, "titulo_pagina": "Editar música", "botao": "Salvar alterações"},
    )


@login_required
def excluir_musica(request, pk):
    musica = get_object_or_404(Musica, pk=pk, usuario=request.user)

    if request.method == "POST":
        musica.delete()
        messages.success(request, "Música excluída do catálogo.")
        return redirect("catalogo:lista")

    return render(request, "catalogo/confirmar_exclusao.html", {"musica": musica})
