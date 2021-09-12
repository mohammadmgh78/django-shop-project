from django.db import models

from customer.models import Customer
from product.models import Product


class Order(models.Model):
    products = models.ManyToManyField(Product)
    number_of_products = models.JSONField()
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    CONFIRMED = 'confirmed'
    CANCELLED = 'cancelled'
    ON_WAY = 'on the way'
    DELIVERED = 'delivered'
    NOT_SELECTED = ''
    choices = (
        (CONFIRMED, 'confirmed'),
        (CANCELLED, 'cancelled'),
        (ON_WAY, 'on the way'),
        (DELIVERED, 'delivered'),
        (NOT_SELECTED, 'Not Selected'),
    )
    order_status = models.CharField(max_length=30, choices=choices, db_index=True,
                                    default=NOT_SELECTED,
                                    help_text='status of the order')
    date_submitted = models.DateField(auto_now=True)

    def __str__(self):
        return f'order of {self.user}'


class OrderHistory(models.Model):
    order = models.OneToOneField(Order, on_delete=models.RESTRICT)
    user = models.ForeignKey(Customer, on_delete=models.RESTRICT)  # thiw might be wrong

    def __str__(self):
        return f'{self.order.__str__()}'
