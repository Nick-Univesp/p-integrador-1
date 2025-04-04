from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, FileResponse
from mysite.settings import MEDIA_ROOT
from .models import Sala, Disciplina, Atividade, Classe, Aula
from django.views import generic
import os

def frontpage(request):
    return render(request, "escola/frontpage.html")
    
def media(request, imagem):
    return FileResponse(open(os.path.join(MEDIA_ROOT, imagem), 'rb'))