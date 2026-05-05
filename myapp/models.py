from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()


class Client(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()

    def __str__(self):
        return self.name
    
class Order(BaseModel):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    status = models.CharField(
        max_length=50,
        default='Pendente'
    )

    def __str__(self):
        return f'Pedido #{self.pk} - {self.client.name}'