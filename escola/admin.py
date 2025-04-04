from django.contrib import admin
from .models import Sala, Disciplina, Atividade, Classe, Aula
import nested_admin

class Sala_Create(admin.ModelAdmin):
    model = Sala

class Disciplina_Create(admin.ModelAdmin):
    model = Disciplina

class Atividade_Create(admin.ModelAdmin):
    model = Atividade

class Classe_Create(admin.ModelAdmin):
    model = Classe

class Aula_Create(admin.ModelAdmin):
    model = Aula

admin.site.register(Sala, Sala_Create)
admin.site.register(Disciplina, Disciplina_Create)
admin.site.register(Atividade, Atividade_Create)
admin.site.register(Classe, Classe_Create)
admin.site.register(Aula, Aula_Create)
