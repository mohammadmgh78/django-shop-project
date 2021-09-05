from django.db import models

from customer.models import Customer


class Discount(models.Model):
    discount = models.IntegerField()

    def __str__(self):
        return self.discount


class Order(models.Model):
    products = models.JSONField()
    number_of_products = models.JSONField()
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f'order of {self.user}'


class OrderHistory(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.order.__str__()}'
