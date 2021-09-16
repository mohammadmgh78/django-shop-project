from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    image = models.ImageField(upload_to='img', blank=True)
    name = models.CharField(max_length=80)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

