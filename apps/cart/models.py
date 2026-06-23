from django.db import models
from apps.common.base_models import UUIDModel, TimeStampedModel
from apps.accounts.models import User
from apps.catalog.models import ProductVariant

class Cart(UUIDModel, TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart")
    
class CartItem(UUIDModel, TimeStampedModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    variant = models.ForeignKey(ProductVariant, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    
    class Meta:
        unique_together = ("cart", "variant")
        
