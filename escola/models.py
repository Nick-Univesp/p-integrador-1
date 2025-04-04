from django.db import models
from django.db.models import Value
from django.conf import settings


# Variáveis
semana = {
    "SEGUNDA": "Segunda=feira",
    "TERCA": "Terça-feira",
    "QUARTA": "Quarta-feira",
    "QUINTA": "Quinta-feira",
    "SEXTA": "Sexta-feira"
}

anos = {
    "1" : "1° Ano",
    "2" : "2° Ano",
    "3" : "3° Ano",
    "4" : "4° Ano",
    "5" : "5° Ano",
    "6" : "6° Ano",
    "7" : "7° Ano",
    "8" : "8° Ano",
    "9" : "9° Ano"
}


# função por "paulox" (https://www.paulox.net/2023/11/24/database-generated-columns-part-2-django-and-postgresql/#a-calculated-concatenated-field)
# está função é necessária devido a uma incompatibilidade da função Concat padrão do Django
class ConcatOp(models.Func):
    arg_joiner = " || "
    function = None
    output_field = models.TextField()
    template = "%(expressions)s"



class Sala(models.Model):
    numero = models.IntegerField(verbose_name= "Número", unique=True)
    def __str__(self):
        return str(self.numero)
        
class Disciplina(models.Model):
    nome = models.CharField(verbose_name= "Matéria", unique=True)
    def __str__(self):
        return self.nome
    
class Atividade(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    inicio = models.DateField
    entrega = models.DateField

class Classe(models.Model):
    ano = models.CharField(choices=anos)
    turma = models.CharField(max_length=10)
    expression=ConcatOp('ano', Value(' '), "turma"),
    def __str__(self):
        return self.expression

class Aula(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    dia = models.CharField(choices=semana)
    horario = models.TimeField(verbose_name="Horário")
    duracao = models.DurationField(verbose_name="Duração")