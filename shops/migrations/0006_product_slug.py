# Generated by Django 5.1 on 2024-09-09 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0005_alter_product_category_alter_product_is_available_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', verbose_name='لینک'),
        ),
    ]