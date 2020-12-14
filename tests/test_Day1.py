import pytest
from day1 import report_repair

def test_index_value():
    expenses = [1, 2, 3]
    assert report_repair(expenses) == 0
