from django.db import models
from django.db.models.fields.related import OneToOneField
from project.models import Pledge
#
#
# Create your models here.
class Payment(models.Model):
    pledge = OneToOneField(
                Pledge,
                related_name='payment',
                on_delete=models.CASCADE,
                )
    merchant_order_no = models.CharField(max_length=50)
    total = models.IntegerField()
    status = models.CharField(max_length=50)
    paid_date = models.CharField(max_length=50, blank=True)
    expired_date = models.CharField(max_length=50, blank=True)
    bank_code = models.CharField(max_length=10, blank=True)
    code_no = models.CharField(max_length=50, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)