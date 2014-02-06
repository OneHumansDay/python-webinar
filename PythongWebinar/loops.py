class CartItem:
    def __init__(self, name, price):
        self.price = price
        self.name = name

    def __repr__(self):
        return "({0}, ${1})".format(self.name, self.price)

class ShoppingCart:
    def __init__(self,):
        self.__items = []

    def add(self, cart_item):
        self.__items.append(cart_item)

    @property
    def total_price(self):
        total = 0.0
        for itm in self.__items:
            total += item.price

        return total;

cart = ShoppingCart()
cart.add(CartItem("CD", 19.99))
cart.add(CartItem("Record", 17.99))


print("Total price is ${0:,}".format(cart.total_price));