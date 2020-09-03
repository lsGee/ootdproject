from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo, name="photo"),
    path('<int:list>/', views.photo, name="photo"),
    path('likeCount/', views.likeCount, name="likeCount"),
    path('dislikeCount/', views.dislikeCount, name="dislikeCount"),
]