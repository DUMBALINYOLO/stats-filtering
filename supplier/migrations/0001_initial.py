# Generated by Django 2.2 on 2020-02-17 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, null=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_primary', models.CharField(blank=True, max_length=16)),
                ('phone_secondary', models.CharField(blank=True, max_length=16)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('region', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('ghpgps', models.CharField(blank=True, max_length=16)),
                ('comment', models.TextField(blank=True)),
            ],
        ),
    ]
