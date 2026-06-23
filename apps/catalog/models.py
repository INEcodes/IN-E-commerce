from django.db import models
from apps.common.base_models import UUIDModel, TimeStampedModel

class Category(UUIDModel, TimeStampedModel):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, related_name="children")
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class Product(UUIDModel, TimeStampedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products")
    base_price = models.DecimalField(max_digits=12, decimal_places=2)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    
class ProductVariant(UUIDModel, TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")
    sku = models.CharField(max_length=100, unique=True)
    color = models.CharField(max_length=50,blank=True)
    price = models.DecimalField(max_digits=12,decimal_places=2)
    attributes = models.JSONField(default=dict, blank=True)
    is_active = models.BooleanField(default=True)