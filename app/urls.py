from django.contrib.auth import views as auth_views
from django.urls import path

from .views import DocumentoCreateView, DocumentoListView

urlpatterns = [
    # Autenticação
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Documentos
    path('', DocumentoListView.as_view(), name='lista_documentos'),
    path('documentos/novo/', DocumentoCreateView.as_view(), name='novo_documento'),
]
