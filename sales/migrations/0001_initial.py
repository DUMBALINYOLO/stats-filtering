# Generated by Django 2.2 on 2020-02-17 21:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
        ('invoice', '0001_initial'),
        ('cash', '0001_initial'),
        ('customer', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('receipt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditSalesReturn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('cp', models.DecimalField(decimal_places=3, max_digits=10)),
                ('sp', models.DecimalField(decimal_places=3, max_digits=10)),
                ('product_name', models.CharField(max_length=50, null=True)),
                ('comment', models.CharField(blank=True, default='', max_length=256)),
                ('is_voided', models.BooleanField(blank=True, default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('customer_name', models.CharField(blank=True, default='', max_length=256)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.Customer')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('invoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='invoice.SalesReturnInvoice')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CreditSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('cp', models.DecimalField(decimal_places=3, max_digits=10)),
                ('sp', models.DecimalField(decimal_places=3, max_digits=10)),
                ('product_name', models.CharField(max_length=50, null=True)),
                ('comment', models.CharField(blank=True, default='', max_length=256)),
                ('is_voided', models.BooleanField(blank=True, default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('customer_name', models.CharField(blank=True, default='', max_length=256)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.Customer')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('invoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='invoice.SalesInvoice')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CashSalesReturn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('cp', models.DecimalField(decimal_places=3, max_digits=10)),
                ('sp', models.DecimalField(decimal_places=3, max_digits=10)),
                ('product_name', models.CharField(max_length=50, null=True)),
                ('comment', models.CharField(blank=True, default='', max_length=256)),
                ('is_voided', models.BooleanField(blank=True, default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('customer_name', models.CharField(blank=True, default='', max_length=256)),
                ('system', models.CharField(blank=True, default='Physical Cash', max_length=256)),
                ('currency', models.CharField(blank=True, default='', max_length=64)),
                ('cash', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cash.Cash')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.Product')),
                ('receipt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='receipt.SalesReturnReceipt')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CashSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('cp', models.DecimalField(decimal_places=3, max_digits=10)),
                ('sp', models.DecimalField(decimal_places=3, max_digits=10)),
                ('product_name', models.CharField(max_length=50, null=True)),
                ('comment', models.CharField(blank=True, default='', max_length=256)),
                ('is_voided', models.BooleanField(blank=True, default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('customer_name', models.CharField(blank=True, default='', max_length=256)),
                ('system', models.CharField(blank=True, default='Physical Cash', max_length=256)),
                ('currency', models.CharField(blank=True, default='', max_length=64)),
                ('cash', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cash.Cash')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.Product')),
                ('receipt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='receipt.SalesReceipt')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
