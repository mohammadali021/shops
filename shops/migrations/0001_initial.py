# Generated by Django 5.1 on 2024-08-29 16:52

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'دسته بندی محصول',
                'verbose_name_plural': 'دسته بندی',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='نام')),
                ('last_name', models.CharField(max_length=100, verbose_name='نام خانوادگی')),
                ('phone', models.CharField(max_length=100, verbose_name='شماره تماس')),
                ('email', models.EmailField(max_length=100, verbose_name='ایمیل')),
                ('password', models.CharField(max_length=100, verbose_name='رمز عبور')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام محصول')),
                ('description', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('rate', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('picture', models.ImageField(upload_to='images/products/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pro_category', to='shops.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('address', models.CharField(blank=True, default='', max_length=100)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.product')),
            ],
        ),
    ]
