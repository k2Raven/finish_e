# Generated by Django 2.2 on 2020-03-14 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20200314_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filebase',
            name='access',
            field=models.CharField(choices=[('Common', 'Общий'), ('Hidden', 'Скрытый'), ('Private', 'Приватный')], default='Common', max_length=200, verbose_name='Доступ'),
        ),
    ]
