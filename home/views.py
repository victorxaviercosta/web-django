from django.shortcuts import render, redirect
from django.utils.text import slugify

from .forms import MessageForm
from .models import Message, Tag


def index(request):
    messages = Message.objects.all()
    return render(request, "home/index.html", {"mensagens": messages})

def sobre(request):
    return render(request, "home/sobre.html")

def new_message(request):
    from django.contrib import messages

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            # 1. Salva título, conteúdo, autor e categoria no banco.
            message = form.save()

            # 2. Transforma o texto digitado em objetos Tag e associa à mensagem.
            tags_texto = form.cleaned_data["tags"]
            for split in tags_texto.split(","):
                name = slugify(split)
                if name:
                    tag, _ = Tag.objects.get_or_create(name=name)
                    message.tags.add(tag)

            # Mensagem de sucesso
            messages.success(request, "Mensagem publicada com sucesso!")

            # 3. Redireciona para a página inicial (padrão Post/Redirect/Get).
            return redirect("index")
    else:
        form = MessageForm()

    return render(request, "home/nova.html", {"form": form})