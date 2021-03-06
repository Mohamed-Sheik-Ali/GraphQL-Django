# Generated by Django 3.2.9 on 2021-12-03 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='workmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=15)),
                ('workflow', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Parties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(max_length=18)),
                ('account_number', models.CharField(max_length=18)),
                ('name', models.CharField(max_length=35)),
                ('base_currency', models.CharField(max_length=3)),
                ('address_line_1', models.CharField(max_length=35)),
                ('address_line_2', models.CharField(max_length=35)),
                ('city', models.CharField(max_length=35)),
                ('state', models.CharField(max_length=35)),
                ('zipcode', models.CharField(max_length=6)),
                ('country_code', models.CharField(max_length=2)),
                ('customer', models.BooleanField(default=False)),
                ('model_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='transactions.workmodel')),
            ],
        ),
    ]
