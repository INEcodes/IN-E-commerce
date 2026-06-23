from django.db import models
from apps.common.base_models import UUIDModel, TimeStampedModel
from apps.catalog.models import ProductVariant

class Inventory(UUIDModel, TimeStampedModel):
    variant = models.OneToOneField(ProductVariant, on_delete=models.CASCADE, related_name="inventory")
    quantity = models.PositiveIntegerField(default=0)
    reserved_quantity = models.PositiveIntegerField(default=0)
    
    @property
    def available_quantity(self):
        return self.quantity - self.reserved_quantity