from django.db import models
from django.db.models import Value
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Q
from datetime import datetime
from django.forms import ModelForm


# Dicionários
semana = {
    "SEGUNDA": "Segunda-feira",
    "TERCA": "Terça-feira",
    "QUARTA": "Quarta-feira",
    "QUINTA": "Quinta-feira",
    "SEXTA": "Sexta-feira"
}

anos = {
    "1° Ano" : "1° Ano",
    "2° Ano" : "2° Ano",
    "3° Ano" : "3° Ano",
    "4° Ano" : "4° Ano",
    "5° Ano" : "5° Ano",
    "6° Ano" : "6° Ano",
    "7° Ano" : "7° Ano",
    "8° Ano" : "8° Ano",
    "9° Ano" : "9° Ano"
}



class Classe(models.Model):
    ano = models.CharField(choices=anos)
    turma = models.CharField(max_length=10)
    alunos = models.ManyToManyField(
        User,
        related_name="alunos_0",
        limit_choices_to= Q(groups__name = "Alunos")
        )
    def __str__(self):
        nome = str(self.ano) + ' ' + str(self.turma)
        return nome



class Aula(models.Model):
    disciplina = models.CharField(max_length=50)
    sala = models.PositiveSmallIntegerField(blank=True, null=True)
    classe = models.ForeignKey(
        Classe,
        on_delete=models.CASCADE
        )
    dia = models.CharField(choices=semana)
    horario = models.TimeField(verbose_name="Horário")
    professor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="professor_0"
        )
    info = models.TextField(verbose_name="Informação", blank=True, null=True) 
    def __str__(self):
        nome = str(self.disciplina) + ' | ' + str(Classe.objects.get(pk=self.classe_id))
        return nome



class Atividade(models.Model):
    disciplina = models.CharField(max_length=50)
    inicio = models.DateField()
    entrega = models.DateField(blank=True, null=True)
    professor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="professor_1",
        limit_choices_to= Q(groups__name = "Professores")
        )
    classe = models.ManyToManyField(
        Classe,
        related_name="classe_1",
        )
    content = models.TextField(verbose_name="Conteúdo", blank=True, null=True)
    def __str__(self):
        nome = str(self.disciplina) + ' | ' + str(self.inicio)
        return nome



class Comunicado(models.Model):
    remetente = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="remetente_0",
        verbose_name="Remetente",
        editable=False
        )
    data = models.DateField(auto_now_add=True)
    destinatarios = models.ManyToManyField(
        User,
        related_name="destinatarios_0",
        verbose_name="Destinatários"
        )
    mensagem = models.TextField()
    data = models.DateField(auto_now_add=True)
    def __str__(self):
        nome = str(self.remetente) + ' | ' + str(self.data)
        return nome