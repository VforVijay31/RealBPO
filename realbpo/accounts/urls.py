from django.urls import path
from accounts import views

urlpatterns = [
    # Owner login
    path('login/owner/', views.owner_login, name='owner_login'),

    # Employee login
    path('login/employee/', views.employee_login, name='employee_login'),

    # Register (with role selection)
    path('register/', views.register_user, name='register_user'),

    # Logout
    path('logout/', views.logout_user, name='logout'),

    # Employee dashboard
    path('employee/dashboard/', views.employee_dashboard, name='employee_dashboard'),
    #create employee
    path("create-employee/", views.create_employee, name="create_employee"),
]