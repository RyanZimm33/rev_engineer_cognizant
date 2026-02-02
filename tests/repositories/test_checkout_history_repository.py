from src.domain.checkout_history import CheckoutHistory
from src.repositories.checkout_history_repository import CheckoutHistoryRepository

def test_get_all_checkout_history():
    filepath = "tests/test_checkout_history.json"
    repo = CheckoutHistoryRepository(filepath)

    history = repo.get_all_checkout_history()

    assert history[0].book_id == "test"
    assert history[1].book_id == "b1db8afe-d8c8-4809-bf4c-9c2c4cadd463"

def test_add_checkout_history():
    filepath = "tests/test_checkout_history.json"
    repo = CheckoutHistoryRepository(filepath)
    history = CheckoutHistory(book_id="test_add", check_in="2024")

    added_history = repo.add_checkout_history(history)

    assert added_history == "test_add"

def test_find_checkout_history_by_book_id():
    filepath = "tests/test_checkout_history.json"
    repo = CheckoutHistoryRepository(filepath)
    book_id = "test_add"

    history = repo.find_checkout_history_by_book_id(book_id)[0]

    assert history.book_id == "test_add"
    assert history.check_in == "2024"
