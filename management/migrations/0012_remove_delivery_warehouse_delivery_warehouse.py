# Generated by Django 4.0.10 on 2023-06-27 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0011_productwarehouse_remove_delivery_warehouse_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='warehouse',
        ),
        migrations.AddField(
            model_name='delivery',
            name='warehouse',
            field=models.ForeignKey(blank=True, help_text='Выберите склад для поставки', null=True, on_delete=django.db.models.deletion.CASCADE, to='management.warehouse'),
        ),
    ]