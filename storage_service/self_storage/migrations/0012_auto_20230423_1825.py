# Generated by Django 3.2 on 2023-04-23 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('self_storage', '0011_auto_20230423_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='cost',
            field=models.PositiveSmallIntegerField(default=2579, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='order',
            name='qr_code',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='QR-код для доступа'),
        ),
    ]