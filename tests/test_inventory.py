import json
from pathlib import Path

import pytest

from inventory.pricing import apply_discount, with_tax
from inventory.report import low_stock
from inventory.store import Store

ROOT = Path(__file__).resolve().parent.parent


def test_add_and_remove_stock():
    store = Store()
    store.add_item("apple", 10, price=0.5)
    store.add_item("apple", 5)
    store.remove_item("apple", 3)
    assert store.quantity("apple") == 11


def test_cannot_oversell():
    store = Store()
    store.add_item("pear", 1)
    with pytest.raises(ValueError):
        store.remove_item("pear", 2)


def test_pricing():
    assert with_tax(100, 0.08) == 108.0
    assert apply_discount(100, "SAVE10") == 90.0
    assert apply_discount(100, "BOGUS") == 100


def test_low_stock_report():
    store = Store()
    store.add_item("a", 2)
    store.add_item("b", 50)
    assert low_stock(store, 5) == [("a", 2)]


def test_config_is_valid_json():
    config = json.loads((ROOT / "config" / "settings.json").read_text())
    assert config["low_stock_threshold"] == 5
