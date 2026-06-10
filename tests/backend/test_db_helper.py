import pytest
from backend import db_helper
from datetime import date

# @pytest.fixture
# def db():
#     with get_db_cursor() as cursor:
#         return cursor


def test_fetch_expense_for_date():
    test_date = date(2024, 8, 15)
    expenses = db_helper.fetch_expenses_for_date("2024-08-15")
    assert expenses[0]['expense_date'] == test_date
    assert expenses[0]['amount'] == 10
    assert expenses[0]['category'] == 'Shopping'
    assert len(expenses) == 1


def test_fetch_expense_for_invalid_date():
    test_date = date(9999, 9, 15)
    expenses = db_helper.fetch_expenses_for_date("9999-09-15")
    assert len(expenses) == 0


def test_insert_expense():
    db_helper.insert_expense("2025-01-01", 1000, "Shopping", "Clothing")
    expenses = db_helper.fetch_expenses_for_date("2025-01-01")
    assert len(expenses) == 1
    assert expenses[0]["amount"] == 1000
    assert expenses[0]["category"] == "Shopping"