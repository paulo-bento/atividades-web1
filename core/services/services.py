from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from core.repositories.repositories import PedidoRepository


class PedidoService:
    @staticmethod
    def criar_pedido(usuario, dados_form):
        pedido = PedidoRepository.criar_pedido(
            usuario=usuario,
            titulo=dados_form.cleaned_data['titulo'],
            descricao=dados_form.cleaned_data['descricao'],
            status='pendente',
            arquivo=dados_form.cleaned_data['arquivo']
        )
        PedidoService.enviar_email_confirmacao(pedido)
        return pedido

    @staticmethod
    def enviar_email_confirmacao(pedido):
        assunto = 'Confirmação de Pedido'
        contexto = {
            'usuario': pedido.usuario,
            'pedido': pedido
        }
        corpo = render_to_string('emails/pedido_confirmado.html', contexto)

        email = EmailMessage(
            subject=assunto,
            body=corpo,
            to=[pedido.usuario.email],
        )
        email.content_subtype = 'html'
        email.send()
