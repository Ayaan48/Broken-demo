"""Low-stock report."""



def low_stock(store, threshold):
    rows = []

    for sku, item in sorted(store.items.items()):
        if item["quantity"] <= threshold:
            rows.append((sku, item["quantity"]))

    return rows
