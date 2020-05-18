from django.shortcuts import redirect


def staff_required(func):
    def wrapper(*args, **kwargs):
        request = args[1]
        if request.user.is_staff:
            return func(*args, **kwargs)
        else:
            return redirect('login')

    return wrapper
