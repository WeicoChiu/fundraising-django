from django.contrib import admin
from .models import Payment

# Register your models here.
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'merchant_order_no', 'total',
        'status', 'paid_date',
        'expired_date', 'bank_code',
        'code_no')
