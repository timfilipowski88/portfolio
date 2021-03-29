from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.index),
    path('index/', views.index, name = 'index'),
    path('get_collection_form', views.get_collection_form, name='get_collection_form'),
    path('add_collection/', views.add_collection, name = 'add_collection'),
    path('update_collection/<int:collection_id>', views.update_collection, name='update_collection'),
    path('add_assignment/', views.add_assignment, name='add_assignment'),
    path('get_assignment_form', views.get_assignment_form, name='get_assignment_form'),
    path('update_assignment/<int:assignment_id>', views.update_assignment, name='update_assignment'),
]
