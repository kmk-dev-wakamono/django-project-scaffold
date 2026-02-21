from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/<str:user>/', views.greet, name='greet'),
    path('hello/rev/<str:user>/', views.reverse_greet, name='reverse_greet'),
]
