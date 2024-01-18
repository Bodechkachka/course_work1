from django.db import models

class Office(models.Model):
    office_id = models.AutoField(db_column='id', primary_key=True)
    office_name = models.CharField(db_column='Название офиса', max_length=100)
    office_address = models.CharField(db_column='Адрес', unique=True, max_length=200)
    office_contacts = models.CharField(db_column='Контакты', unique=True, max_length=30)

    def __str__(self):
        return self.office_name

    class Meta:
        verbose_name = 'Офис'
        verbose_name_plural = 'Офисы'

class Rate(models.Model):
    rate_id = models.AutoField(db_column='id', primary_key=True)
    tariff_name = models.CharField(db_column='Название', max_length=100)
    tariff_rate = models.FloatField(db_column='Тарифная ставка')
    contract_term = models.IntegerField(db_column='Срок действия', blank=True, null=True)

    def __str__(self):
        return self.tariff_name

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

class Client(models.Model):
    client_id = models.AutoField(db_column='id', primary_key=True)
    full_name = models.CharField(db_column='Полное имя', max_length=100)
    birth_date = models.DateField(db_column='Дата рождения')
    passport_id = models.PositiveBigIntegerField(db_column='Номер паспорта', unique=True)
    client_contacts = models.CharField(db_column='Контакты', unique=True, max_length=30)
    client_address = models.CharField(db_column='Адрес', unique=True, max_length=100)
    client_segment = models.CharField(db_column='Сегмент', max_length=15)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Agent(models.Model):
    agent_id = models.AutoField(db_column='id', primary_key=True)
    full_name = models.CharField(db_column='Полное имя', max_length=100)
    agent_contacts = models.CharField(db_column='Контакты', unique=True, max_length=30)
    office_id = models.ForeignKey(Office, models.DO_NOTHING, db_column='id офиса', blank=True, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Агент'
        verbose_name_plural = 'Агенты'

class Object(models.Model):
    object_id = models.AutoField(db_column='id', primary_key=True)  # Field name made lowercase.
    object_name = models.CharField(db_column='Название', max_length=50)  # Field name made lowercase.
    object_description = models.CharField(db_column='Описание', max_length=200, blank=True, null=True)

    def __str__(self):
        return self.object_name

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

class Contract(models.Model):
    contract_number = models.PositiveBigIntegerField(db_column='Номер договора', primary_key=True)
    client_id = models.ForeignKey(Client, models.DO_NOTHING, db_column='id клиента', blank=True, null=True)
    rate_id = models.ForeignKey(Rate, models.DO_NOTHING, db_column='id тарифа', blank=True, null=True)
    object_id = models.ForeignKey(Object, models.DO_NOTHING, db_column='id объекта', blank=True, null=True)
    dococ = models.DateField(db_column='Дата подписания')
    sum_insured = models.PositiveIntegerField(db_column='Страховая сумма')

    def __str__(self):
        return self.contract_number

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'
