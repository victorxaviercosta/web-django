from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sobre/", views.sobre, name="sobre"),
    path("nova/", views.new_message, name="nova_mensagem"),
    path("mensagens/<int:id>/editar/", views.edit_message, name="editar_mensagem"),
    path("mensagens/<int:id>/remover/", views.remove_message, name="remover_mensagem"),
]