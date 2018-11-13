from django.urls import path
from . import views

app_name = 'Employee'
urlpatterns = [
    # ex: /Employee/
    path('', views.index, name='index'),
    # ex: /Employee/5/
    path('<int:employee_id>/', views.detail, name='detail'),
    # ex: /Employee/add_emp/
    path('add_emp/', views.add_employee, name='add_emp'),
    # email_emp
    path('email_emp/', views.email_employee, name='email_emp'),
]
