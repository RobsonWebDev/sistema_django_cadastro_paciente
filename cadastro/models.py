from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class PessoaModel(models.Model):
    nome = models.CharField(max_length=256)
    sobrenome = models.CharField(max_length=256)
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=14)
    data_de_nascimento = models.DateField()
    prim_fone = models.CharField(max_length=64)
    segu_fone = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=128, unique=True)
    id_pessoa_cr = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Dono')
    medico = models.BooleanField(default=False)


class EnderecoModel(models.Model):
    
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=64)
    numero = models.CharField(max_length=8)
    bairro = models.CharField(max_length=64)
    cidade = models.CharField(max_length=64)
    uf = models.CharField(max_length=2)
    complemento = models.CharField(max_length=128)
    id_pessoa = models.ForeignKey(PessoaModel, on_delete=models.SET_NULL, blank=True, null=True)
    

class RegistroModel(models.Model):
 
    titulo = models.CharField(max_length=64)
    numero = models.CharField(max_length=12, unique=True)
    inscricao = models.CharField(max_length=10)
    situacao = models.CharField(max_length=10)
    id_pessoa = models.ForeignKey(PessoaModel, on_delete=models.CASCADE,blank=True, null=True)


class EspecialidadeModel(models.Model):

    area = models.CharField(max_length=64)
    rqe = models.CharField(max_length=10, unique=True)
    id_registro = models.ForeignKey(PessoaModel, on_delete=models.CASCADE,blank=True, null=True)


class HistoricoModel(models.Model):

    id_pessoa_cr = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Dono')
    id_pessoa_pa = models.ForeignKey(PessoaModel, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Paciente')
    data_consulta = models.DateTimeField()
    prontuario = models.FileField()
    data_de_criacao = models.DateTimeField(default=timezone.now)
