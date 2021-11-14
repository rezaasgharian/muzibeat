from django.contrib import admin
from .models import Post, category


# Register your models here.
class categoryadmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'position')
    list_filter = (['status'])
    prepopulated_fields = {'title': ('title',)}
    search_fields = ('title',)


admin.site.register(category, categoryadmin)


class postAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish','category_to_str', 'status')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', 'publish']
    def category_to_str(self,obj):
        return ",".join([category.title for category in obj.category.all()])


admin.site.register(Post, postAdmin)
