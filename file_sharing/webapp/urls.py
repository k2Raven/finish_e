from django.urls import path
from webapp.views.file_views import FilePage, FileAddPage

app_name = 'webapp'

urlpatterns = [
    path('', FilePage.as_view(), name='index'),
    path('add/', FileAddPage.as_view(), name='file_add')
]
