from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo, name="photo"),
    path('<int:list>/', views.photo, name="photo"),
    path('likeCount/', views.likeCount, name="likeCount"),
    path('dislikeCount/', views.dislikeCount, name="dislikeCount"),
    path('index/', views.index, name="index"),
    path('generic/', views.generic, name="generic"),
    path('elements/', views.elements, name="elements"),
]