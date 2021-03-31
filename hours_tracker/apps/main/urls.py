from django.urls import path
from . import views


app_name = "main"
urlpatterns = [
    path('', views.index),
    path('index/', views.index.as_view(), name = 'index'),
    # path('add_collection/', views.add_collection, name = 'add_collection'),
    # path('update_collection/<int:collection_id>', views.update_collection, name='update_collection'),
    path('add_assignment/', views.add_assignment.as_view(), name='add_assignment'),
    # path('update_assignment/<int:assignment_id>', views.update_assignment, name='update_assignment'),
]
