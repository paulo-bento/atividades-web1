from django.contrib import admin

from .models import Pedido


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario', 'status', 'criado_em')
    list_filter = ('status', 'criado_em')
    search_fields = ('titulo', 'usuario__email')
    readonly_fields = ('criado_em', 'atualizado_em')
