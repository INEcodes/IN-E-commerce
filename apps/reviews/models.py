from django.db import models
from apps.common.base_models import UUIDModel, TimeStampedModel
from apps.accounts.models import User
from apps.catalog.models import Product

class Review(UUIDModel, TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)
    is_approved = models.BooleanField(default=False)