from django.urls import path
<<<<<<< HEAD
from .views import Login, Register, Logout_View
=======
from .views import Login, Register , Logout_view
>>>>>>> c1bef300c8a185fd8c7cbf9ca31d620a64f54636

urlpatterns = [
    path('login/', Login, name="login"),
    path('register/', Register, name="register"),
<<<<<<< HEAD
    path('logout/', Logout_View, name="logout"),
=======
    path('logout/', Logout_view, name="Logout_view"),

>>>>>>> c1bef300c8a185fd8c7cbf9ca31d620a64f54636
]