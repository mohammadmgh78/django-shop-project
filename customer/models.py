from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    city_born = models.CharField(max_length=50)
    closest_friend = models.CharField(max_length=50)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Address(models.Model):
    address = models.CharField(max_length=150)
    customer = models.ManyToManyField(Customer)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f'{self.address}'
