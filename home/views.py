from django.shortcuts import render

from .models import Message


def index(request):
    messages = Message.objects.all()
    return render(request, "home/index.html", {"mensagens": messages})

def sobre(request):
    return render(request, "home/sobre.html")
