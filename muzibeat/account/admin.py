from django.contrib import admin
from .models import UserRegister


# class registerAdmin(admin.ModelAdmin):
#     list_display = ('uuid')
#     list_filter = ('uuid',)
#     search_fields = ('uuid', 'username','payment')
admin.site.register(UserRegister)