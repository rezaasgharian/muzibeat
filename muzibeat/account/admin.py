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
        ('user', {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('is_admin',)}),
        ('Permission', {'fields': ('is_active',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'username', 'password', 'password_Confirmation')}),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class UserCreateForm(admin.ModelAdmin):
    readonly_fields = ('uuid',)
    form = UserCreateForm


class UserChangeForm(admin.ModelAdmin):
    readonly_fields = ('uuid',)
    form = UserChangeForm


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']


class Category_User_Admin(admin.ModelAdmin):
    list_display = ('title', 'status')
    list_filter = (['status'])
    prepopulated_fields = {'title': ('title',)}
    search_fields = ('title',)


admin.site.register(Category_user, Category_User_Admin)
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post_user)
admin.site.register(Images)
admin.site.register(Videos)
admin.site.register(Voices)
admin.site.register(Files)

# admin.site.unregister(Group)
