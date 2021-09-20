from django.contrib import admin
from .models import Payment


# Register your models here.
class paymentAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'product_id', 'price', 'ref', 'status', 'date')
    list_filter = ('date', 'status')
    search_fields = ('title', 'description')
    ordering = ['status', 'date']

admin.site.register(Payment,paymentAdmin)