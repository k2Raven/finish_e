from django.db import models
from multiselectfield import MultiSelectField

from django.contrib.auth.models import User


GENERAI_ACCESS_FILECHOICES = (
    ('Common', 'Общий'),
    ('Hidden', 'Скрытый'),
    ('Private', 'Приватный')
)


class FileBase(models.Model):
    name_file = models.CharField(max_length=128, verbose_name='Имя файла')
    file = models.FileField(upload_to='file_base', verbose_name='Фаил')
    access = MultiSelectField(choices=GENERAI_ACCESS_FILECHOICES, default=GENERAI_ACCESS_FILECHOICES[0][0],
                              verbose_name='Доступ')
    author = models.ForeignKey(User, related_name='author_file', verbose_name='автор файла',
                               on_delete=models.SET_NULL, null=True, blank=True)
    creation_date = models.DateTimeField(verbose_name='Дата создание', auto_now=True)
    numder_of_downloads = models.IntegerField(verbose_name='Скачали', default=0)