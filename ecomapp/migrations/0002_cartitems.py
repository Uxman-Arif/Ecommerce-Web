# Generated by Django 5.0.6 on 2024-11-03 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ManyToManyField(blank=True, null=True, to='ecomapp.product')),
            ],
        ),
    ]
