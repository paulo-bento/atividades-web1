from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import DocumentoForm
from .models import Documento


class DocumentoListView(LoginRequiredMixin, ListView):
    model = Documento
    template_name = "documentos/lista.html"
    context_object_name = "documentos"

    def get_queryset(self):
        return Documento.objects.filter(usuario=self.request.user).order_by(
            "-data_envio"
        )


class DocumentoCreateView(LoginRequiredMixin, CreateView):
    model = Documento
    form_class = DocumentoForm
    template_name = "documentos/form.html"
    success_url = reverse_lazy("lista_documentos")

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
