# Generated by Django 5.1 on 2024-08-20 10:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0002_create_country_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='delivery_address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='delivery_city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courier.city'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='delivery_country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courier.country'),
        ),
    ]
