# Generated by Django 5.0 on 2024-01-06 05:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.customermodel')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.servicemodel')),
            ],
            options={
                'indexes': [models.Index(fields=['customer_id', 'service_id'], name='services_or_custome_18ad96_idx'), models.Index(fields=['service_id'], name='services_or_service_2272c7_idx')],
            },
        ),
    ]