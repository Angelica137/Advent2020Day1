import pytest
from day1 import report_repair

def test_add_index_values():
    expenses = [4, 2]
    n = 6
    assert report_repair(expenses, n) == 6
