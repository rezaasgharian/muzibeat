<<<<<<< HEAD:muzibeat/muzibeat/middlewares.py
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
=======
# from django.shortcuts import redirect
# from django.contrib import messages
#
# LOGIN_EXEMPT_URLS = [
#     '/admin/',
#     '/register/',
#     '/logout/',
#
# ]
#
# class LoginMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#     def __call__(self, request):
#         if not request.user.is_authenticated and request.path not in LOGIN_EXEMPT_URLS:
#             messages.error(request, 'you should login first', 'warning')
#             return redirect('login')
#         response = self.get_response(request)
#         return response
>>>>>>> c1bef300c8a185fd8c7cbf9ca31d620a64f54636:muzibeat/account/middlewares.py
