from django.urls import path
from webapp.views.file_views import FilePage, FileAddPage, FileDeletePage, FileDetailPage, FileUpdateView

app_name = 'webapp'

urlpatterns = [
    path('', FilePage.as_view(), name='index'),
    path('add/', FileAddPage.as_view(), name='file_add'),
    path('delete/<int:pk>', FileDeletePage.as_view(), name='delete_file'),
    path('detail/<int:pk>', FileDetailPage.as_view(), name='detail_file'),
    path('update/<int:pk>', FileUpdateView.as_view(), name='update_file')

]
