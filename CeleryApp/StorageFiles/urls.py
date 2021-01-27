from django.urls import path
import StorageFiles.views

urlpatterns = [
    path('', StorageFiles.views.index, name="home"),
    path('files/<username>/', StorageFiles.views.view_files, name="view_files"),
    path('checker/<file_id>', StorageFiles.views.checker, name="checker"),
]


