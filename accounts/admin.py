from django.contrib import admin
from .models import User, Customer, Employee, CustomerId

# Register your models here.

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(CustomerId)
admin.site.register(Employee)