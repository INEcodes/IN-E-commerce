from django.db import models
from apps.common.base_models import UUIDModel, TimeStampedModel
from apps.orders.models import Order

class Shipment(UUIDModel, TimeStampedModel):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="shipment")
    courier = models.CharField(max_length=100)
    tracking_number = models.CharField(max_length=120, blank=True)
    status = models.CharField(max_length=50, default="pending")
    shipped_at = models.DateTimeField(null=True, blank=True)
    delivered_ar = models.DateTimeField(null=True, blank=True)