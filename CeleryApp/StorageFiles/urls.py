from django.urls import path
import StorageFiles.views

urlpatterns = [
    path('', StorageFiles.views.index, name="home")
]


