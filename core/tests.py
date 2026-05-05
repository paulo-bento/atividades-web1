from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase
from django.urls import reverse

from .models import STATUS_CHOICES, Pedido

User = get_user_model()


class PedidoTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.usuario = User.objects.create_user(
            email="teste@example.com",
            password="teste123",
            nome_completo="Usuário Teste",
        )

    def test_redireciona_usuario_nao_autenticado(self):
        response = self.client.get(reverse("lista_pedidos"))
        self.assertRedirects(response, "/login/?next=/")

    def test_criacao_pedido_autenticado(self):
        self.client.login(email="teste@example.com", password="teste123")
        arquivo_teste = SimpleUploadedFile("teste.pdf", b"arquivo conteudo")
        response = self.client.post(
            reverse("novo_pedido"),
            {
                "titulo": "Pedido Teste",
                "descricao": "Descrição de teste",
                "arquivo": arquivo_teste,
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pedido criado com sucesso")
        self.assertEqual(Pedido.objects.count(), 1)
        self.assertEqual(Pedido.objects.first().titulo, "Pedido Teste")

    def test_visualizacao_lista_apenas_do_usuario(self):
        outro_usuario = User.objects.create_user(
            email="outro@example.com", password="123456"
        )
        arquivo1 = SimpleUploadedFile("meu.pdf", b"conteudo")
        arquivo2 = SimpleUploadedFile("outro.pdf", b"conteudo")
        Pedido.objects.create(
            usuario=self.usuario,
            titulo="Meu Pedido",
            status="pendente",
            arquivo=arquivo1,
        )
        Pedido.objects.create(
            usuario=outro_usuario,
            titulo="Outro Pedido",
            status="pendente",
            arquivo=arquivo2,
        )

        self.client.login(email="teste@example.com", password="teste123")
        response = self.client.get(reverse("lista_pedidos"))
        self.assertContains(response, "Meu Pedido")
        self.assertNotContains(response, "Outro Pedido")
