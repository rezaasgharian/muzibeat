from django.shortcuts import redirect
from django.contrib import messages

LOGIN_EXEMPT_URLS = [
    '/login/',
    '/register/',
    '/admin',
]

class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        if not request.user.is_authenticated and request.path not in LOGIN_EXEMPT_URLS:
            messages.error(request, 'you should login first', 'warning')
            return redirect('login')
        response = self.get_response(request)
        # if request.user.is_superuser:
        #     return redirect('admin')
        # elif not request.user.is_superuser:
        #     return redirect('login')
        # response = self.get_response(request)
        return response
