# Generated by Django 3.2.7 on 2021-09-16 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='number_of_products',
            field=models.JSONField(blank=True),
        ),
    ]