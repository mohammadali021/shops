# Generated by Django 5.1 on 2024-09-10 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0007_product_long_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', verbose_name='لینک'),
        ),
    ]