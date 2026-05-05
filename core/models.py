from django.conf import settings
from django.db import models

STATUS_CHOICES = [
    ('pendente', 'Pendente'),
    ('em_progresso', 'Em progresso'),
    ('concluido', 'Concluído'),
    ('cancelado', 'Cancelado'),
]


def upload_path(instance, filename):
    return f'pedidos/usuario_{instance.usuario.id}/{filename}'


class Pedido(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    arquivo = models.FileField(upload_to=upload_path)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.titulo} - {self.status}'
