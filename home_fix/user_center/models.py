from django.db import models


# Create your models here.
class Transaction(models.Model):
    sender = models.CharField(
        "sender email address", max_length=64, blank=True, null=True
    )
    receiver = models.CharField(
        "receiver email address", max_length=64, blank=True, null=True
    )
    amount = models.DecimalField(
        "amount", max_digits=20, decimal_places=2, default=0.0, blank=True, null=True
    )
    commission_fee = models.DecimalField(
        "commission_fee",
        max_digits=20,
        decimal_places=2,
        default=0.0,
        blank=True,
        null=True,
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    service_type = models.CharField("type", max_length=64, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.timestamp.__str__())