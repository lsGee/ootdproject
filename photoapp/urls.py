from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo, name="photo"),
    path('<int:list>/', views.photo, name="photo"),
    path('<int:list>/<int:like>/', views.photo, name="photo"),
]