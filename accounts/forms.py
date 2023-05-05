from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Admin, Customer, Employee
from django.conf import settings

#the user will have to enter the admin code inorder to register as admin
class AdminCodeForm(forms.Form):
    admin_code = forms.CharField(max_length=50)
    def clean_admin_code(self):
        admin_code = self.cleaned_data.get('admin_code')
        if admin_code != settings.ADMIN_CODE:
            raise forms.ValidationError('Invalid admin code')
        return admin_code

#admin registration form
class AdminSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    position = forms.CharField(required=True)
    
    class Meta(UserCreationForm.Meta):
        model = User
    
    #verify email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        admin = Admin.objects.create(user=user)
        admin.phone_number=self.cleaned_data.get('phone_number')
        admin.position=self.cleaned_data.get('position')
        admin.save()
        return user
    
class CustomerSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    location = forms.CharField(required=True) 

    class Meta(UserCreationForm.Meta):
        model = User
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.phone_number=self.cleaned_data.get('phone_number')
        customer.location=self.cleaned_data.get('location')
        customer.save()
        return user

class EmployeeSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    designation = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_staff = True
        user.is_employee = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        employee = Employee.objects.create(user=user)
        employee.phone_number=self.cleaned_data.get('phone_number')
        employee.designation=self.cleaned_data.get('designation')
        employee.save()
        return user
