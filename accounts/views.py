from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from . forms import AdminCodeForm, AdminSignUpForm, CustomerSignUpForm, EmployeeSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
#from .decorators import admin_code_entered


#register general view
def register(request):
    return render(request, 'register.html')


# version1-the admin registration validation view
def admin_validate(request):
    form = AdminCodeForm(request.POST or None)
    if form.is_valid():
        if form.cleaned_data['admin_code'] == settings.ADMIN_CODE:
            return redirect('admin_register')
        else:
            form.add_error('admin_code', 'Incorrect admin code.')
    return render(request, 'admin_code.html', {'form': form})


def admin_register(request):
    if request.method == 'POST':
        form = AdminSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = AdminSignUpForm()
    return render(request, 'admin_register.html', {'form': form})


#function view equivalent for class view customer_register
def customer_register(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = CustomerSignUpForm()
    return render(request, 'customer_register.html', {'form': form})

#function view equivalent for class view employee_register
def employee_register(request):
    if request.method == 'POST':
        form = EmployeeSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = EmployeeSignUpForm()
    return render(request, 'employee_register.html', {'form': form})


#Login view
def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('employee')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    context={
        'form':AuthenticationForm()
    } 
    return render(request, 'login.html', context)
    
#admin page
def admin(request):
    return render(request,'admin.html')

#customer page
def customer(request):
    return render(request,'customer.html')

#employee page
def employee(request):
    return render(request,'employee.html')

def logout_view(request):
    logout(request)
    return redirect('/')

