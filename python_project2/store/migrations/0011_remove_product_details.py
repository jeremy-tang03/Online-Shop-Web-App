# Generated by Django 4.0.4 on 2022-05-05 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_remove_product_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='details',
        ),
    ]
