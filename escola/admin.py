from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.forms import AuthenticationForm
from .models import Atividade, Classe, Aula, Comunicado
import nested_admin
from django.contrib.auth.models import User
from django.db.models import Q



AdminSite.site_header = "Administração"
AdminSite.site_title = "Administração"
AdminSite.index_title = "Administração"

class PortalDoAluno(AdminSite):
    site_header = "Portal do Aluno"
    site_title = "Portal do Aluno"
    index_title = "Portal do Aluno"

    login_form = AuthenticationForm
    def has_permission(self, request):
        return request.user.is_active

portal_do_aluno = PortalDoAluno(name='portal')



class Classe_Create(admin.ModelAdmin):
    model = Classe

    def get_queryset(self, request):
        if request.user in User.objects.filter(Q(is_superuser = True)|Q(groups__name = "Professores")):
            return super().get_queryset(request)
        else:
            return super().get_queryset(request).filter(Q(alunos = request.user))



class Aula_Create(admin.ModelAdmin):
    model = Aula
    
    def get_queryset(self, request):
        if request.user in User.objects.filter(Q(is_superuser = True)):
            return super().get_queryset(request)
        elif request.user in User.objects.filter(Q(groups__name = "Professores")):
            return super().get_queryset(request).filter(Q(professor = request.user))
        else:
            UserClasse = Classe.objects.filter(Q(alunos = request.user.id))
            return super().get_queryset(request).filter(Q(classe__in = UserClasse))

    def has_change_permission(self, request, obj=Aula):
        if request.user in User.objects.filter(Q(is_superuser = True)):
            return super().has_change_permission(request, obj)
        if obj != None and obj.professor == request.user:
            return super().has_change_permission(request, obj)
        
    def has_delete_permission(self, request, obj=Aula):
        if request.user in User.objects.filter(Q(is_superuser = True)):
            return super().has_delete_permission(request, obj)
        elif obj != None and obj.professor == request.user:
            return super().has_delete_permission(request, obj)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.professor = request.user
            return super().save_model(request, obj, form, change)



class Atividade_Create(admin.ModelAdmin):
    model = Atividade

    def get_queryset(self, request):
        if request.user in User.objects.filter(Q(is_superuser = True)):
            return super().get_queryset(request)
        elif request.user in User.objects.filter(Q(groups__name = "Professores")):
            return super().get_queryset(request).filter(Q(professor = request.user))
        else:
            UserClasse = Classe.objects.filter(Q(alunos = request.user.id))
            return super().get_queryset(request).filter(Q(classe__in = UserClasse))

    def has_change_permission(self, request, obj=Atividade):
        if request.user in User.objects.filter(Q(is_superuser = True)):
            return super().has_change_permission(request, obj)
        if obj != None and obj.professor == request.user:
            return super().has_change_permission(request, obj)
        
    def has_delete_permission(self, request, obj=Atividade):
        if request.user in User.objects.filter(Q(is_superuser = True)):
            return super().has_delete_permission(request, obj)
        elif obj != None and obj.professor == request.user:
            return super().has_delete_permission(request, obj)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.professor = request.user
            return super().save_model(request, obj, form, change)



class Comunicado_Create(admin.ModelAdmin):
    model = Comunicado

    def get_queryset(self, request):
        if request.user in User.objects.filter(Q(is_superuser = True)):
            return super().get_queryset(request)
        elif request.user in User.objects.filter(Q(groups__name = "Professores")):
            return super().get_queryset(request).filter(Q(destinatarios = request.user)|Q(remetente = request.user))
        else:
            return super().get_queryset(request).filter(Q(destinatarios = request.user))

    def has_change_permission(self, request, obj=Comunicado):
        if request.user in User.objects.filter(Q(is_superuser = True)):
            return super().has_change_permission(request, obj)
        if obj != None and obj.remetente == request.user:
            return super().has_change_permission(request, obj)
        
    def has_delete_permission(self, request, obj=Comunicado):
        if request.user in User.objects.filter(Q(is_superuser = True)):
            return super().has_delete_permission(request, obj)
        elif obj != None and obj.remetente == request.user:
            return super().has_delete_permission(request, obj)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.remetente = request.user
            return super().save_model(request, obj, form, change)



portal_do_aluno.register(Classe, Classe_Create)
portal_do_aluno.register(Aula, Aula_Create)
portal_do_aluno.register(Atividade, Atividade_Create)
portal_do_aluno.register(Comunicado, Comunicado_Create)
