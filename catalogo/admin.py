from django.contrib import admin
from .models import Musica

@admin.register(Musica)
class MusicaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "artista", "status", "nota", "data_adicao", "usuario")
    list_filter = ("status", "nota")
    search_fields = ("titulo", "artista", "album")
