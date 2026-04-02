"""
Пакет с Page Object классами для тестирования.
"""

from .CalcPage import CalculatorPage
from .LoginPage import LoginPage
from .InvPage import InventoryPage
from .CartPage import CartPage
from .CheckPage import CheckoutPage

__all__ = [
    "CalculatorPage",
    "LoginPage",
    "InventoryPage",
    "CartPage",
    "CheckoutPage",
]
