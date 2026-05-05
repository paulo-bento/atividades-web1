from django.contrib.auth import views as auth_views
from django.urls import path

from .views import PedidoCreateView, PedidoListView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('', PedidoListView.as_view(), name='lista_pedidos'),
    path('novo/', PedidoCreateView.as_view(), name='novo_pedido'),
]
