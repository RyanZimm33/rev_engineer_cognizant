import pytest
from src.domain.checkout_history import CheckoutHistory


def test_get_time():
    history = CheckoutHistory(book_id="test", check_in="8000")

    time = history.get_time()

    assert time[0] == "check_in"
    assert time[1] == "8000"

def test_from_dict():
    dict_history = {"book_id" :"test", "check_out":"2026"}
    history = CheckoutHistory.from_dict(dict_history)
    
    assert history.book_id == "test"
    assert history.check_out == "2026"

def test_to_dict():
    history = CheckoutHistory(book_id="test", check_in="1989")

    dict_book = history.to_dict()

    assert dict_book["book_id"] == "test"
    assert dict_book["check_in"] == "1989"