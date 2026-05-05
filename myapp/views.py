from django.shortcuts import render
from django.db.models import Count, Sum
from .models import Client


def get_clients(request):
    clients = Client.objects.filter(
        is_deleted=False
    ).annotate(
        total_orders=Count('orders'),
        total_spent=Sum('orders__total_price')
    )

    return render(request, 'clients.html', {
        'clients': clients
    })