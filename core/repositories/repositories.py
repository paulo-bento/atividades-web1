from ..models import Pedido


class PedidoRepository:
    @staticmethod
    def criar_pedido(usuario, titulo, descricao, status, arquivo):
        return Pedido.objects.create(
            usuario=usuario,
            titulo=titulo,
            descricao=descricao,
            status=status,
            arquivo=arquivo
        )

    @staticmethod
    def listar_por_usuario(usuario):
        return Pedido.objects.filter(usuario=usuario).order_by('-criado_em')

    @staticmethod
    def alterar_status(pedido_id, novo_status):
        pedido = Pedido.objects.get(id=pedido_id)
        pedido.status = novo_status
        pedido.save()
        return pedido
