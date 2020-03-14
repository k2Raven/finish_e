from django.urls import path
from webapp.views.file_views import FilePage, FileAddPage, FileDeletePage

app_name = 'webapp'

urlpatterns = [
    path('', FilePage.as_view(), name='index'),
    path('add/', FileAddPage.as_view(), name='file_add'),
    path('<int:pk>/delete/', FileDeletePage.as_view(), name='delete_file')
]
