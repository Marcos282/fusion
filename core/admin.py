from django.contrib import admin
from .models import Servico, Cargo, Funcionario


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'descricao', 'ativo', 'criados', 'modificado')
    list_display_links = ('cargo',)
    search_fields = ('cargo',)
    list_filter = ('ativo', 'criados', 'modificado')
    list_editable = ('ativo',)


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):   
    list_display = ('servico', 'descricao', 'icone', 'ativo', 'criados', 'modificado')
    list_display_links = ('servico',)
    search_fields = ('servico',)
    list_filter = ('ativo', 'criados', 'modificado')
    list_editable = ('ativo',)

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'criados', 'modificado')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_filter = ('ativo', 'criados', 'modificado')
    list_editable = ('ativo',)