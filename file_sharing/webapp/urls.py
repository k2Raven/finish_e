from django.urls import path
from webapp.views.file_views import FilePage

app_name = 'webapp'

urlpatterns = [
    path('', FilePage.as_view(), name='index')
]
