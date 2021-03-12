# Generated by Django 2.2 on 2020-02-17 21:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('desc', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('cp', models.DecimalField(decimal_places=3, max_digits=10)),
                ('sp', models.DecimalField(decimal_places=3, max_digits=10)),
                ('quantity', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('min_stock', models.PositiveIntegerField(blank=True, default=1)),
                ('max_stock', models.PositiveIntegerField(blank=True, default=100)),
                ('unit_of_measure', models.CharField(blank=True, max_length=8)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.Category')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryIncrement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, null=True)),
                ('cp', models.DecimalField(decimal_places=3, max_digits=10)),
                ('sp', models.DecimalField(decimal_places=3, max_digits=10)),
                ('quantity', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('tempq', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('comment', models.CharField(default='Increase', max_length=256)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InventoryDecrement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, null=True)),
                ('cp', models.DecimalField(decimal_places=3, max_digits=10)),
                ('sp', models.DecimalField(decimal_places=3, max_digits=10)),
                ('quantity', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('tempq', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('comment', models.CharField(default='Decrease', max_length=256)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]