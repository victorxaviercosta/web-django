from django import forms

from .models import Message

# Classe Tailwind reaproveitada por todos os campos do formulário.
INPUT = (
    "w-full rounded-lg bg-slate-800 border border-white/10 px-3 py-2 "
    "text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-400"
)


class MessageForm(forms.ModelForm):
    # Campo extra (não existe no model): o visitante digita as tags como texto
    # livre separado por vírgula. Vamos transformá-lo em objetos Tag na view.
    tags = forms.CharField(
        required=False,
        label="Tags",
        help_text="Separe por vírgula. Ex.: django, tutorial, iniciante",
        widget=forms.TextInput(attrs={"class": INPUT}),
    )

    class Meta:
        model = Message
        fields = ["title", "content", "author", "category"]
        labels = {
            "title": "Título",
            "content": "Conteúdo",
            "author": "Autor",
            "category": "Categoria",
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": INPUT}),
            "content": forms.Textarea(attrs={"class": INPUT, "rows": 4}),
            "author": forms.TextInput(attrs={"class": INPUT}),
            "category": forms.Select(attrs={"class": INPUT}),
        }