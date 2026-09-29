"""Low-stock report."""

import csv
import datetime
from collections import OrderedDict


def low_stock(store, threshold):
    rows = []
    
    for sku, item in sorted(store.items.items()):
        if item["quantity"] <= threshold:
            rows.append((sku, item["quantity"]))
    
    return rows