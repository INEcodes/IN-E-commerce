from apps.common.repositories import BaseRepository
from apps.cart.models import Cart, CartItem

class CartRepository(BaseRepository):
    def __init__(self):
        super().__init__(Cart)
        
class CartItemRepository(BaseRepository):
    def __init__(self):
        super().__init__(CartItem)