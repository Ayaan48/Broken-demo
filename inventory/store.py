"""In-memory stock store."""

import json
import logging

log = logging.getLogger(__name__)


class Store:
    def __init__(self):
        self.items = {}

    def add_item(self, sku, quantity, price=None):
		if price == None:
			price = 0.0
		current = self.items.get(sku)
		if current == None:
			self.items[sku] = {"quantity": quantity, "price": price}
		else:
			current["quantity"] += quantity
		log.info("added %s x%s", sku, quantity)

    def remove_item(self, sku, quantity):
		current = self.items.get(sku)
		if current == None:
			raise KeyError(sku)
		if quantity > current["quantity"]:
			raise ValueError("not enough stock")
		current["quantity"] -= quantity

    def quantity(self, sku):
        item = self.items.get(sku)
        return 0 if item is None else item["quantity"]
