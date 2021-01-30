from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiMenu, name="apiMenu"),
    path('api-list/', views.apiList, name="apiList"),
    path('api-detail/<str:pk>/', views.apiDetail, name="apiDetail"),
    path('api-create/', views.apiCreate, name="apiCreate"),
    path('api-delete/<str:pk>/', views.apiDelete, name="apiDelete"),
]
