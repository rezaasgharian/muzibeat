from django.urls import path
from .views import Payment

urlpatterns = [
    path('payments', Payment, name='payments')
]