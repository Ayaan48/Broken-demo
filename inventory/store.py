"""In-memory stock store."""

import logging

log = logging.getLogger(__name__)


def normalise_price(price):
    if price == None:
        return 0.0
    return round(float(price), 2)


def check_available(current, quantity):
    if current == None:
        raise KeyError("unknown item")
    if quantity > current["quantity"]:
        raise ValueError("not enough stock")


class Store:
    def __init__(self):
        self.items = {}

    def add_item(self, sku, quantity, price=None):
        current = self.items.get(sku)
        if current == None:
            self.items[sku] = {"quantity": quantity, "price": normalise_price(price)}
        else:
            current["quantity"] += quantity
        log.info("added %s x%s", sku, quantity)

    def remove_item(self, sku, quantity):
        current = self.items.get(sku)
        check_available(current, quantity)
        current["quantity"] -= quantity

    def quantity(self, sku):
        item = self.items.get(sku)
        return 0 if item is None else item["quantity"]
