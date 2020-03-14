from django import forms
from webapp.models import FileBase


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')


class FileAnonForm(forms.ModelForm):
    class Meta:
        model = FileBase
        exclude = ['creation_date', 'numder_of_downloads', 'author', 'access']


class FileForm(forms.ModelForm):
    class Meta:
        model = FileBase
        exclude = ['creation_date', 'numder_of_downloads', 'author']