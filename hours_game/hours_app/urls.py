from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_reg, name='log_reg'),
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('context/', views.context, name = 'context'),
    path('add_collection/', views.add_collection, name = 'add_collection'), 
    path('add_assignment/', views.add_assignment, name = 'add_assignment'),
    path('update_assignment/<int:id>', views.update_assignment, name = 'update_assignment'),
    path('update_collection/<int:id>', views.update_collection, name = 'update_collection'),
    path('delete_assignment/<int:id>', views.delete_assignment, name = 'delete_assignment'),
    path('delete_collection/<int:id>', views.delete_collection, name = 'delete_collection'),
    path('calculate_hours/', views.calculate_hours, name = 'calculate_hours'),
]