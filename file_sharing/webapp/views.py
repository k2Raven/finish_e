from django.shortcuts import render
from django.views.generic import ListView
from webapp.models import FileBase


class FilePage(ListView):
    template_name = 'index.html'
    context_object_name = 'file_all'
    paginate_by = 10
    paginate_orphans = 1

    def get_queryset(self):
        return FileBase.objects.all().order_by('-creation_date')

