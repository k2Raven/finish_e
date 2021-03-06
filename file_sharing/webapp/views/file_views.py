from django.db.models import Q
from webapp.models import FileBase
from django.http import HttpResponseRedirect
from .base_view import SearchView
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from webapp.forms import FileAnonForm, FileForm

from django.urls import reverse_lazy




class FilePage(SearchView):
    template_name = 'index.html'
    context_object_name = 'files'
    ordering = ['-creation_date']
    model = FileBase
    paginate_by = 2
    paginate_orphans = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['files'] = FileBase.objects.filter(access='Common')
        return context

    def get_query(self):
        val = super().get_query()
        query = Q(name__icontains=val)
        return query


class FileAddPage(CreateView):
    model = FileBase
    template_name = 'file_create.html'
    success_url = '/'

    def get_form_class(self):
        if self.request.user.is_authenticated:
            self.form_class = FileForm
        else:
            self.form_class = FileAnonForm
        return self.form_class

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        return super().form_valid(form)


class FileDetailPage(DetailView):
    template_name = 'file_detail.html'
    model = FileBase


class FileDeletePage(DeleteView):
    template_name = 'file/delete.html'
    model = FileBase
    success_url = reverse_lazy('webapp:index')


class FileUpdateView(UpdateView):
    template_name = 'file_update.html'
    model = FileBase
    form_class = FileForm

