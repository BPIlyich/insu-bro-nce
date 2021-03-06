# Generated by Django 3.2.5 on 2021-07-18 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('percent_rate', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='percent rate')),
                ('term', models.CharField(choices=[('month', 'month'), ('year', 'year')], max_length=10, verbose_name='term')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'verbose_name': 'insurance product',
                'verbose_name_plural': 'insurance products',
                'db_table': 'insurance_product',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='InsuranceProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
            ],
            options={
                'verbose_name': 'insurance category',
                'verbose_name_plural': 'insurance categories',
                'db_table': 'insurance category',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='InsuranceProductResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='What should I call you?', max_length=100, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('phone', models.CharField(max_length=16, verbose_name='phone')),
                ('comment', models.TextField(verbose_name='comment')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('insurance_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insurance_responses', to='insurance.insuranceproduct', verbose_name='insurance product')),
            ],
            options={
                'verbose_name': 'insurance product response',
                'verbose_name_plural': 'insurance product responses',
                'db_table': 'insurance_product_response',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='insuranceproduct',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insurance_products', to='insurance.insuranceproductcategory', verbose_name='category'),
        ),
        migrations.AddField(
            model_name='insuranceproduct',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insurance_products', to=settings.AUTH_USER_MODEL, verbose_name='created by'),
        ),
    ]
