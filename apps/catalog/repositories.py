from apps.common.repositories import BaseRepository
from apps.catalog.models import Product, Category, ProductVariant

class ProductRepository(BaseRepository):
    def __init__(self):
        super().__init__(Product)
        
    def get_active_products(self):
        return self.model.objects.filter(is_active=True).select_related("category")
    
class CategoryRepository(BaseRepository):
    def __init__(self):
        super().__init__(Category)
        
class ProductVarientRepository(BaseRepository):
    def __init__(self):
        super().__init__(ProductVariant)