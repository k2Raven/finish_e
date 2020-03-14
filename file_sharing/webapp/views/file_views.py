from django.db.models import Q
from webapp.models import FileBase
from .base_view import SearchView



class FilePage(SearchView):
    template_name = 'index.html'
    context_object_name = 'files'
    ordering = ['-creation_date']
    model = FileBase
    paginate_by = 2
    paginate_orphans = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_query(self):
        val = super().get_query()
        query = Q(name__icontains=val)
        return query


