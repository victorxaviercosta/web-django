from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.contrib import messages


from .forms import MessageForm
from .models import Message, Tag


def _parse_tags(message, tags_text):
    """Substitui as tags da mensagem pelas que vieram do formulário."""

    message.tags.clear()
    for split in tags_text.split(","):
        name = slugify(split)
        if name:
            tag, _ = Tag.objects.get_or_create(name=name)
            message.tags.add(tag)


def index(request):
    messages = Message.objects.all()
    return render(request, "home/index.html", {"mensagens": messages})

def sobre(request):
    return render(request, "home/sobre.html")

def new_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            # 1. Salva título, conteúdo, autor e categoria no banco.
            message = form.save()

            _parse_tags(message, form.cleaned_data["tags"])

            # Mensagem de sucesso
            messages.success(request, "Mensagem publicada com sucesso!")

            # 3. Redireciona para a página inicial (padrão Post/Redirect/Get).
            return redirect("index")
    else:
        form = MessageForm()

    return render(request, "home/nova.html", {"form": form})

def edit_message(request, id):
    message = get_object_or_404(Message, id=id)

    if request.method == "POST":
        form = MessageForm(request.POST, instance=message)

        if form.is_valid():
            message = form.save()
            _parse_tags(message, form.cleaned_data["tags"])
            messages.success(request, "Mensagem atualizada com sucesso!")

            return redirect("index")
    else:
        current_tags = ", ".join(tag.name for tag in message.tags.all())
        form = MessageForm(instance=message, initial={"tags": current_tags})

    return render(request, "home/editar.html", {"form": form, "message": message})


def remove_message(request, id):
    message = get_object_or_404(Message, id=id)

    if request.method == "POST":
        message.delete()
        messages.success(request, "Mensagem removida.")
        return redirect("index")

    return render(request, "home/remover.html", {"message": message})