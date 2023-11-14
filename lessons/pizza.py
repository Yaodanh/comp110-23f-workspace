"""Defing a class!"""

from _future_ import annotations

class Pizza: 
    #<name>: <type>
    size: str
    toppings: int
    gluten_free: bool

    def _init_(self, inp_size: str, inp_toppings: int, inp_gf: bool):
        self.size = inp_size
        self.toppings = inp_toppings
        self.gluten_free = inp_gf
        # returns a Pizza object

    def price(self) -> float:
        """Calculate price of pizza."""
        if self.size == "large":
            price: float = 6.25
        else:
            price: float = 5.00
        price += .75 * self.toppings
        if self.gluten_free:
            price += 1.00
        return price
    
    def add_toppings(self, num_toppings: int):
        """Add toppings to existence pizza."""
        self.toppings += num_toppings

    def make_new_pizza_add_toppings(self, num_toppings: int) -> Pizza:
        new_pizza: Pizza = Pizza(self.size, self.toppings + num_toppings)