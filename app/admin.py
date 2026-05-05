import os

from django.contrib import admin
from django.utils.html import format_html

from .models import Categoria, CustomUser, Documento


class TamanhoArquivoFilter(admin.SimpleListFilter):
    title = "Tamanho do Arquivo"
    parameter_name = "tamanho"

    def lookups(self, request, model_admin):
        return [
            ("pequeno", "Até 1MB"),
            ("medio", "1MB a 2MB"),
            ("grande", "Acima de 2MB"),
        ]

    def queryset(self, request, queryset):
        if self.value() == "pequeno":
            return queryset.filter(arquivo__size__lte=1 * 1024 * 1024)
        if self.value() == "medio":
            return queryset.filter(
                arquivo__size__gt=1 * 1024 * 1024, arquivo__size__lte=2 * 1024 * 1024
            )
        if self.value() == "grande":
            return queryset.filter(arquivo__size__gt=2 * 1024 * 1024)
        return queryset


class DataEnvioFilter(admin.SimpleListFilter):
    title = "Data de Envio"
    parameter_name = "data_envio"

    def lookups(self, request, model_admin):
        return [
            ("hoje", "Hoje"),
            ("semana", "Últimos 7 dias"),
            ("mes", "Últimos 30 dias"),
        ]

    def queryset(self, request, queryset):
        import datetime

        from django.utils import timezone

        hoje = timezone.now().date()
        if self.value() == "hoje":
            return queryset.filter(data_envio__date=hoje)
        if self.value() == "semana":
            return queryset.filter(
                data_envio__date__gte=hoje - datetime.timedelta(days=7)
            )
        if self.value() == "mes":
            return queryset.filter(
                data_envio__date__gte=hoje - datetime.timedelta(days=30)
            )
        return queryset


@admin.action(description="Marcar como Verificado")
def marcar_como_verificado(modeladmin, request, queryset):
    queryset.update(verificado=True)
    modeladmin.message_user(
        request, f"{queryset.count()} documentos marcados como verificados."
    )


class DocumentoInline(admin.TabularInline):
    model = Documento
    extra = 1


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    inlines = [DocumentoInline]


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = (
        "arquivo_nome",
        "usuario",
        "categoria",
        "data_envio",
        "verificado",
        "visualizar_arquivo",
    )
    list_filter = ("categoria", TamanhoArquivoFilter, DataEnvioFilter, "verificado")
    actions = [marcar_como_verificado]

    def arquivo_nome(self, obj):
        return os.path.basename(obj.arquivo.name)

    def visualizar_arquivo(self, obj):
        if obj.arquivo:
            return format_html(
                f"<a href='{obj.arquivo.url}' target='_blank'>Visualizar</a>"
            )
        return "-"

    visualizar_arquivo.short_description = "Arquivo"


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email", "nome_completo", "is_staff", "is_active")
    search_fields = ("email", "nome_completo")
