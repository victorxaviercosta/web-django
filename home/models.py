from django.db import models


class Mensagem(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    creation_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-creation_timestamp"]

    def __str__(self):
        return self.titulo