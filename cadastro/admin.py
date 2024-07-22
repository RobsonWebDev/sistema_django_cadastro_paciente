from django.contrib import admin
from .models import PessoaModel, EnderecoModel, RegistroModel, EspecialidadeModel, HistoricoModel
from django.contrib.auth import admin as admin_auth_django


@admin.register(PessoaModel)
class PessoaAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome', 'sobrenome', 'email', 'medico',
    list_editable= 'medico',



admin.site.register(EnderecoModel)
admin.site.register(RegistroModel)
admin.site.register(EspecialidadeModel)
@admin.register(HistoricoModel)
class HistoricoAdmin(admin.ModelAdmin):
    pass