# Generated by Django 5.0.1 on 2024-01-14 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('full_name', models.CharField(db_column='Полное имя', max_length=100)),
                ('birth_date', models.DateField(db_column='Дата рождения')),
                ('passport_id', models.PositiveBigIntegerField(db_column='Номер паспорта', unique=True)),
                ('client_contacts', models.CharField(db_column='Контакты', max_length=30, unique=True)),
                ('client_address', models.CharField(db_column='Адрес', max_length=100, unique=True)),
                ('client_segment', models.CharField(db_column='Сегмент', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('object_id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('object_name', models.CharField(db_column='Название', max_length=50)),
                ('object_description', models.CharField(blank=True, db_column='Описание', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('office_id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('office_name', models.CharField(db_column='Название офиса', max_length=100)),
                ('office_address', models.CharField(db_column='Адрес', max_length=200, unique=True)),
                ('office_contacts', models.CharField(db_column='Контакты', max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('rate_id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('tariff_name', models.CharField(db_column='Название', max_length=100)),
                ('tariff_rate', models.FloatField(db_column='Тарифная ставка')),
                ('contract_term', models.IntegerField(blank=True, db_column='Срок действия', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('agent_id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('full_name', models.CharField(db_column='Полное имя', max_length=100)),
                ('agent_contacts', models.CharField(db_column='Контакты', max_length=30, unique=True)),
                ('office_id', models.ForeignKey(blank=True, db_column='id офиса', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.office')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('contract_number', models.PositiveBigIntegerField(db_column='Номер договора', primary_key=True, serialize=False)),
                ('dococ', models.DateField(db_column='Дата подписания')),
                ('sum_insured', models.PositiveIntegerField(db_column='Страховая сумма')),
                ('client_id', models.ForeignKey(blank=True, db_column='id клиента', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.client')),
                ('object_id', models.ForeignKey(blank=True, db_column='id объекта', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.object')),
                ('rate_id', models.ForeignKey(blank=True, db_column='id тарифа', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.rate')),
            ],
        ),
    ]