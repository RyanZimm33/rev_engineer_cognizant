import pytest
from src.domain.checkout_history import CheckoutHistory
from tests.mocks.mock_checkout_history_repository import MockCheckoutHistoryRepo
from src.services.checkout_history_service import CheckoutHistoryService

def test_get_all_checkout_history():
    repo = MockCheckoutHistoryRepo()
    srv = CheckoutHistoryService(repo)

    history = srv.get_all_checkout_history()

    assert len(history) == 1
    assert history[0].book_id == "test"
    assert history[0].check_in == "2020"

def test_find_checkout_history_by_book_id_positive():
    repo = MockCheckoutHistoryRepo()
    srv = CheckoutHistoryService(repo)
    book_id = "test"
    
    history = srv.find_checkout_history_by_book_id(book_id)

    assert history[0].book_id == "test"

def test_find_checkout_history_by_book_id_negative():
    repo = MockCheckoutHistoryRepo()
    srv = CheckoutHistoryService(repo)
    book_id = 5

    with pytest.raises(TypeError) as e:
        srv.find_checkout_history_by_book_id(book_id)
        assert str(e.value) == 'Expected String, got something else'

def test_add_checkout_history_positive():
    repo = MockCheckoutHistoryRepo()
    srv = CheckoutHistoryService(repo)
    history = CheckoutHistory(book_id="test_add", check_in="test")

    book_id = srv.add_checkout_history(history)
    
    assert book_id == "test_add"

def test_add_checkout_history_negative():
    repo = MockCheckoutHistoryRepo()
    srv = CheckoutHistoryService(repo)
    history = 5

    with pytest.raises(TypeError) as e:
        srv.add_checkout_history(history)
        assert str(e.value) == 'Expected Checkout History, got something else'