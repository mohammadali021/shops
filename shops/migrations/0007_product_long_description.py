# Generated by Django 5.1 on 2024-09-09 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0006_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='long_description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
