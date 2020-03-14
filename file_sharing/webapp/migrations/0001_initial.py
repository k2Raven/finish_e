# Generated by Django 2.2 on 2020-03-14 06:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FileBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_file', models.CharField(max_length=128, verbose_name='Имя файла')),
                ('file', models.FileField(blank=True, default='file_base/file_def.jpg', null=True, upload_to='file_base', verbose_name='Фото')),
                ('access', multiselectfield.db.fields.MultiSelectField(choices=[('Common', 'Общий'), ('Hidden', 'Скрытый'), ('Private', 'Приватный')], default='Common', max_length=21, verbose_name='Доступ')),
                ('creation_date', models.DateTimeField(auto_now=True, verbose_name='Дата создание')),
                ('numder_of_downloads', models.IntegerField(default=0, verbose_name='Скачали')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author_file', to=settings.AUTH_USER_MODEL, verbose_name='автор файла')),
            ],
        ),
    ]
