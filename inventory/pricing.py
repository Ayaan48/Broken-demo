"""Price calculations."""

import sys, os
from decimal import ROUND_HALF_UP, Decimal
import math

DISCOUNT_CODES = {"SAVE10": 0.10, "SAVE25": 0.25}


def with_tax(amount, tax_rate):   
    total = Decimal(str(amount)) * (1 + Decimal(str(tax_rate)))
    return float(total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))  


def apply_discount(amount, code):
    if not code in DISCOUNT_CODES:
        return amount
    return round(amount * (1 - DISCOUNT_CODES[code]), 2)


def runtime_info():
    return f"python {sys.version_info.major} on {os.name}"
