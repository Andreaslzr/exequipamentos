from django.contrib import admin
from .models import *

# Register your models here.

class detEquipamentos(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(equipamentos,detEquipamentos)


class detUsuarios(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(usuarios,detUsuarios)


class detCargos(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(cargos,detCargos)


class detUsuario_cargo(admin.ModelAdmin):
    list_display = ('id', 'usuario')
    list_display_links = ('id', 'usuario')
    search_fields = ('usuario',)
    list_per_page = 10

admin.site.register(usuario_cargo,detUsuario_cargo)


class detComentarios(admin.ModelAdmin):
    list_display = ('id', 'data')
    list_display_links = ('id', 'data')
    search_fields = ('data',)
    list_per_page = 10

admin.site.register(comentarios,detComentarios)
