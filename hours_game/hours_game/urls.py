"""hours_game URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hours_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hours_app.urls')),
    # path('hours_app/', views.AssignmentView.as_view(), name='assignment_view'),
    # path('assignment_delete/', views.AssignmentDelete.as_view, name = 'assignment_delete'),    

    # path('hours_app/add_assignment/', views.AddAssignment.as_view(), name='add_assignment'),
]
