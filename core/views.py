from core.repositories.repositories import PedidoRepository
from core.services.services import PedidoService
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import PedidoForm
from .models import Pedido


class PedidoListView(LoginRequiredMixin, ListView):
    model = Pedido
    template_name = "pedidos/lista.html"
    context_object_name = "pedidos"

    def get_queryset(self):
        return PedidoRepository.listar_por_usuario(self.request.user)


class PedidoCreateView(LoginRequiredMixin, CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = "pedidos/form.html"
    success_url = reverse_lazy("lista_pedidos")

    def form_valid(self, form):
        PedidoService.criar_pedido(self.request.user, form)
        messages.success(self.request, "Pedido criado com sucesso.")
        return HttpResponseRedirect(self.success_url)
