# Generated by Django 5.0.6 on 2024-11-03 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0002_cartitems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='item',
            field=models.ManyToManyField(to='ecomapp.product'),
        ),
    ]
