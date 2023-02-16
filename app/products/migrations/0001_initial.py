# Generated by Django 4.1.6 on 2023-02-16 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('sku', models.CharField(max_length=50, verbose_name='SKU')),
                ('type', models.CharField(choices=[('product', 'Product'), ('consumable', 'Consumable'), ('service', 'Service')], default='product', max_length=50, verbose_name='Type')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'product',
            },
        ),
        migrations.AddConstraint(
            model_name='product',
            constraint=models.UniqueConstraint(fields=('name',), name='products_product: name must be unique!'),
        ),
    ]
