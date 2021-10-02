from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *


# class registerAdmin(admin.ModelAdmin):
#     list_display = ('uuid')
#     list_filter = ('uuid',)
#     search_fields = ('uuid', 'username','payment')
admin.site.register(MyUserManager)
admin.site.register(User)