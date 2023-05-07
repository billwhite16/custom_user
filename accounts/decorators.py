from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy, reverse
from django.conf import settings
from . forms import AdminCodeForm
"""
#version 1
def admin_code_entered(function=None):
    actual_decorator = user_passes_test(
        lambda u: hasattr(u, 'admin_code_entered') and u.admin_code_entered == settings.ADMIN_CODE,
        login_url=reverse_lazy('admin_validate'),
        redirect_field_name=None
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
"""
"""
#version 3
def admin_code_entered(view_func):
    def wrap(request, *args, **kwargs):
        if request.method == 'POST':
            form = AdminCodeForm(request.POST)
            if form.is_valid():
                admin_code = form.cleaned_data['admin_code']
                if admin_code == settings.ADMIN_CODE:
                    return view_func(request, *args, **kwargs)
        else:
            form = AdminCodeForm()
        return render(request, 'admin_code.html', {'form': form})
    return wrap
"""






