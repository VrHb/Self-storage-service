# Generated by Django 3.2.18 on 2023-04-19 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Бокс №1', max_length=20, verbose_name='Название бокса')),
                ('floor', models.IntegerField(help_text='3', verbose_name='Номер этажа')),
                ('occupied', models.BooleanField(db_index=True, default=False, verbose_name='Занят')),
                ('end_date', models.DateField(db_index=True, default=django.utils.timezone.now, verbose_name='Дата окончания хранения')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='boxes', to=settings.AUTH_USER_MODEL, verbose_name='Кем занят')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.FloatField(choices=[(0.5, 'Полка'), (1.5, 'Балкон'), (3, 'Кладовка'), (6, 'Комната'), (9, 'Гараж'), (18, 'Чердак')], verbose_name='Наименование размера')),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Склад на Арбате', max_length=30, verbose_name='Название склада')),
                ('address', models.TextField(help_text='г.Москва, ул.Подольских курсантов, д.5', verbose_name='Адрес склада')),
                ('number_of_floors', models.IntegerField(help_text='3', verbose_name='Количество этажей')),
                ('boxes_per_floor', models.IntegerField(help_text='3', verbose_name='Количество боксов на этаже')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='Заказ без номера', max_length=20, verbose_name='Название заказа')),
                ('price', models.IntegerField(db_index=True, verbose_name='Стоимость заказа')),
                ('paid', models.BooleanField(db_index=True, default=False, verbose_name='Оплачен')),
                ('end_date', models.DateField(db_index=True, default=django.utils.timezone.now, verbose_name='Дата окончания хранения')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Дата создания заказа')),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='self_storage.box', verbose_name='Бокс')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Заказчик')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='self_storage.warehouse', verbose_name='Склад')),
            ],
        ),
        migrations.AddField(
            model_name='box',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='boxes', to='self_storage.size', verbose_name='Объём бокса'),
        ),
        migrations.AddField(
            model_name='box',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boxes', to='self_storage.warehouse', verbose_name='Склад'),
        ),
    ]
