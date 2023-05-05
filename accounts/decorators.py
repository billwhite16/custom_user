from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.conf import settings

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
