"""
URL configuration for realbpo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path,include
from home import views
from accounts import views as accounts_views


urlpatterns = [
    path("", views.index, name='home'),
    path("about/", views.about, name='about'),
    path("dashboard/", views.dashboard, name='dashboard'),

    # Projects
    path("projects/create/", views.create_project, name='create_project'),
    path("projects/", views.project_list, name='project_list'),
    path("projects/<int:project_id>/view/", views.view_project, name="view_project"),
    path("projects/<int:project_id>/update/", views.update_project, name="update_project"),
    path("projects/<int:project_id>/delete/", views.delete_project, name="delete_project"),
    path("projects/<int:project_id>/add-service/", views.add_service, name="add_service"),

    # Services
    path("services/<int:service_id>/edit/", views.edit_service, name="edit_service"),

    # Employee
    path("employee_dashboard/", accounts_views.employee_dashboard, name="employee_dashboard"),
]
