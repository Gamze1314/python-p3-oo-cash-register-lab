#!/usr/bin/env python3

class CashRegister():

    def __init__(self, discount=0, total=0, items=None):
        # breakpoint()
        # This way, each instance will have its own separate list object for items
        self.items = items if items is not None else []
        self.discount = discount
        self.total = total if discount is not None else total

    def add_item(self, title, price, quantity=1):
        # stores the item as a dictionary with properties like 'title', 'price', and 'quantity'. The last_transaction method returns the last item dictionary from the items list.
        self.last_item = price
        self.quantity = quantity
        for i in range(quantity):
            self.items.append(title)

        self.total += price * quantity
        return int(self.total)
        # breakpoint()

    def apply_discount(self):
        # total attribute is accesible within any instance method using 'self'
        # apply discount to total price
        if self.discount == 0:
            print("There is no discount to apply.")
            return self.total
        else:
            discounted_total = self.total - \
                int((self.total * self.discount) / 100)
            # breakpoint()
            self.total = discounted_total
            print(
                f"After the discount, the total comes to ${discounted_total}.")
            return discounted_total

    def items_list(self):
        return self.items

    def void_last_transaction(self):
        if len(self.items) > 0:
            updated_total = self.total - (self.last_item * self.quantity)
            self.total = updated_total
            # breakpoint()
        else:
            self.total = 0.0

# how do I access the removed item's price?

# my_register = CashRegister(20, 100, 1000)
# print(my_register)
# my_register.add_item("eggs", 10)
# my_register.add_item("tomato", 5)
# print(my_register.items)
