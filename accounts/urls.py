from django.urls import path
from .import  views

urlpatterns=[
     #registration urls
     path('register/', views.register, name='register'),
     path('register/admin_validate/', views.admin_validate, name='admin_validate'),
     path('register/admin_register/',views.admin_register, name='admin_register'),     
     path('register/customer_register/', views.customer_register, name='customer_register'),
     path('register/employee_register/', views.employee_register, name='employee_register'),
     
     #roles urls
     path('adminpage', views.admin, name='adminpage'),
     path('customer', views.customer, name='customer'),
     path('employee', views.employee, name='employee'),
     
     #login-logout urls
     path('login/', views.login_request, name='login'),
     path('logout/', views.logout_view, name='logout'),
]