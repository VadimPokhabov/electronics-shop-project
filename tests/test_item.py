"""Здесь надо написать тесты с использованием pytest для модуля item."""


def test_calculate_total_price(price=10000, quantity=20):
    assert price * quantity == 200000


def test_apply_discount(price=10000, pay_rate=0.8):
    assert price * pay_rate == 8000
