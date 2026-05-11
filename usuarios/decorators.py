from django.contrib.auth.decorators import user_passes_test

def solo_admin(function=None):
    def check_admin(user):
        return user.is_authenticated and user.is_superuser
    actual_decorator = user_passes_test(check_admin, login_url='/accounts/login/')
    if function:
        return actual_decorator(function)
    return actual_decorator