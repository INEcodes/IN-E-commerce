from django.db import models
from apps.common.base_models import UUIDModel, TimeStampedModel

class Coupon(UUIDModel, TimeStampedModel):
    code = models.CharField(max_length=50, unique=True)
    discount_percent = models.PositiveIntegerField(default=0)
    min_order_value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    expires_at = models.DateTimeField(null=True, blank=True)