from django.contrib import admin
from .models import Client, Order


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'birth_date',
        'is_deleted',
        'created_at',
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'client',
        'product_name',
        'quantity',
        'total_price',
        'created_at',
    ]