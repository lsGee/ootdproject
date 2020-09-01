from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload, name="upload"),
    path('select/', views.uploadsel, name="uploadsel"),
]