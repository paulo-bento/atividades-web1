from django.urls import path

from .views import DocumentoCreateView, DocumentoListView

urlpatterns = [
    path("documentos/", DocumentoListView.as_view(), name="lista_documentos"),
    path("documentos/novo/", DocumentoCreateView.as_view(), name="novo_documento"),
]
