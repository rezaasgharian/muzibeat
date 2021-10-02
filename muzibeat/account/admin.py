from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import *
from .forms import *


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreateForm
    list_display = ('email', 'username')
    list_filter = ('email', 'is_active')
    fieldsets = (
        ('user', {'fields':('email','password')}),
        ('Personal Info', {'fields':('is_admin',)}),
        ('Permission', {'fields':('is_active',)}),
    )
    add_fieldsets = (
        (None, {'fields':('email','username','password1','password2')}),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

class UserCreateForm(admin.ModelAdmin):
    readonly_fields=('uuid',)
    form = UserCreateForm

class UserChangeForm(admin.ModelAdmin):
    readonly_fields=('uuid',)
    form = UserChangeForm

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)