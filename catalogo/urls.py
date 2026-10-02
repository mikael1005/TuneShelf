from django.urls import path
from . import views

app_name = "catalogo"

urlpatterns = [
    path("", views.lista_musicas, name="lista"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("musica/adicionar/", views.adicionar_musica, name="adicionar"),
    path("musica/<int:pk>/editar/", views.editar_musica, name="editar"),
    path("musica/<int:pk>/excluir/", views.excluir_musica, name="excluir"),
]
