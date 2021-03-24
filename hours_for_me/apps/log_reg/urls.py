from django.urls import path
from . import views

app_name = "log_reg"
urlpatterns = [
    path('', views.index,),
    path('index/', views.index, name = "index"),
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
]