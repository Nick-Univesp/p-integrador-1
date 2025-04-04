from django.urls import path
from . import views

urlpatterns = [
    path("", views.frontpage, name="frontpage"),
    path("media/<str:imagem>/",views.media, name="media")
]