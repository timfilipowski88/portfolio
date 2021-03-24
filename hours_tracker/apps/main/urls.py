from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.index),
    path('index/', views.index, name = 'index'),
    path('add_collection/', views.add_collection, name = 'add_collection'),
    path('add_assignment/', views.add_assignment, name='add_assignment'),
]
